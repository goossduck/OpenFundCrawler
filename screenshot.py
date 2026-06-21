import subprocess
import sys
import os

def install_package(package):
    args = [sys.executable, '-m', 'pip', 'install', package]
    print(f"Installing {package}...")
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error installing {package}: {result.stderr}")
        return False
    print(f"{package} installed successfully")
    return True

def main():
    try:
        from playwright.sync_api import sync_playwright
        
        print("Starting browser...")
        with sync_playwright() as p:
            print("Launching Chromium...")
            browser = p.chromium.launch(headless=True)
            print("Creating new page...")
            page = browser.new_page()
            print("Navigating to https://www.sxist.edu.cn...")
            page.goto("https://www.sxist.edu.cn")
            print("Waiting for page to load...")
            page.wait_for_load_state("networkidle")
            print("Taking screenshot...")
            page.screenshot(path="shanxi_tech_university.png", full_page=True)
            browser.close()
            print("Screenshot saved as shanxi_tech_university.png")
    
    except ImportError:
        print("Playwright not found, installing...")
        install_package('playwright')
        print("Re-running script...")
        subprocess.run([sys.executable, __file__])

if __name__ == "__main__":
    main()