#!/usr/bin/env python3
"""
sync_youtube_diet.py — Headless YouTube Watch History Extractor & Cognitive Ingestion Engine.
Pulls recent YouTube watch activity from Brave Browser, categorizes consumption diet,
and updates the MIND Graph visualizer.
"""

import os
import sys
import json
import sqlite3
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# Paths
MIND_DIR = Path(r"c:\Users\sar1s\Documents\MyWork\Git\lifeos-hq\00-control\MIND")
LOG_FILE = MIND_DIR / "youtube_consumption_log.json"
GRAPH_GEN_SCRIPT = MIND_DIR / "generate_graph.py"

BRAVE_HISTORY_PATH = Path(os.path.expandvars(r"%LOCALAPPDATA%\BraveSoftware\Brave-Browser\User Data\Default\History"))

CATEGORIES = {
    "SYSTEMS_AI": [
        "antigravity", "agent", "agents", "hermes", "ai", "llm", "n8n", "workflow", 
        "architecture", "python", "software", "engineering", "roadmap"
    ],
    "CONTENT_MEDIA": [
        "davinci", "resolve", "thumbnail", "editing", "video", "youtube", "storytelling",
        "script", "whisper", "premiere", "audio", "sfx"
    ],
    "HUSTLE_PORN": [
        "clipping", "1 lakh", "first 1 lakh", "make money", "side hustle", "passive income", 
        "whop", "vyro", "agency 2026", "start an ai automation agency"
    ],
    "DECOMPRESSION": [
        "music", "song", "sidhu", "moose wala", "shayari", "elias", "elia", "rahman", "ramayan", "gameplay"
    ]
}

def classify_title(title: str) -> str:
    lower = title.lower()
    # Hustle check first (high priority for cognitive audit)
    for kw in CATEGORIES["HUSTLE_PORN"]:
        if kw in lower:
            return "HUSTLE_PORN"
    for kw in CATEGORIES["CONTENT_MEDIA"]:
        if kw in lower:
            return "CONTENT_MEDIA"
    for kw in CATEGORIES["SYSTEMS_AI"]:
        if kw in lower:
            return "SYSTEMS_AI"
    for kw in CATEGORIES["DECOMPRESSION"]:
        if kw in lower:
            return "DECOMPRESSION"
    return "UNCATEGORIZED"

def fetch_recent_history(limit=50):
    if not BRAVE_HISTORY_PATH.exists():
        print(f"[ERROR] Brave history not found at {BRAVE_HISTORY_PATH}")
        return []

    temp_db = MIND_DIR / "temp_history.db"
    try:
        shutil.copyfile(BRAVE_HISTORY_PATH, temp_db)
        conn = sqlite3.connect(temp_db)
        c = conn.cursor()

        query = """
        SELECT title, url, datetime(last_visit_time/1000000-11644473600, 'unixepoch', 'localtime') as visit_time
        FROM urls 
        WHERE url LIKE '%youtube.com/watch%'
        ORDER BY last_visit_time DESC 
        LIMIT ?
        """
        c.execute(query, (limit,))
        records = []
        for title, url, visit_time in c.fetchall():
            if not title or title.strip() == "YouTube":
                continue
            clean_title = title.replace(" - YouTube", "").strip()
            category = classify_title(clean_title)
            records.append({
                "title": clean_title,
                "url": url,
                "timestamp": visit_time,
                "category": category
            })
        conn.close()
        return records
    finally:
        if temp_db.exists():
            temp_db.unlink()

def run_sync():
    records = fetch_recent_history(limit=50)
    if not records:
        print("[INFO] No YouTube history records fetched.")
        return

    # Tally categories
    breakdown = {"SYSTEMS_AI": 0, "CONTENT_MEDIA": 0, "HUSTLE_PORN": 0, "DECOMPRESSION": 0, "UNCATEGORIZED": 0}
    for r in records:
        breakdown[r["category"]] = breakdown.get(r["category"], 0) + 1

    summary = {
        "last_sync": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_analyzed": len(records),
        "breakdown": breakdown,
        "recent_videos": records[:15]
    }

    LOG_FILE.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"[SUCCESS] Synced {len(records)} videos to {LOG_FILE.name}")
    print(f"Breakdown: {breakdown}")

    # Re-generate Graph HTML
    if GRAPH_GEN_SCRIPT.exists():
        subprocess.run([sys.executable, str(GRAPH_GEN_SCRIPT)], check=False)
        print("[SUCCESS] Re-generated GRAPH_VIEW.html galaxy visualizer.")

if __name__ == "__main__":
    run_sync()
