"""
Playwright keyboard and file-transfer lesson covering keyboard shortcuts, uploads, multiple files, and downloads. This file focuses on fileuploads solution.
"""

import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Page

# Test case covering the single file upload scenario.
@pytest.mark.skip
def test_single_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # Upload single file
    page.locator("#filesToUpload").set_input_files("uploads/Test1.txt")

    # Validate file uploaded
    expect(page.locator("#fileList li")).to_have_text("Test1.txt")
    page.wait_for_timeout(5000)



# Test case covering the multiple file upload scenario.
def test_multiple_file_upload(page:Page):
    page.goto("https://davidwalsh.name/demo/multiple-file-upload.php")

    # Upload multiple files
    files = ["uploads/Test1.txt", "uploads/Test2.txt"]
    page.locator("#filesToUpload").set_input_files(files)

    # Validate file names
    expect(page.locator("#fileList").locator("li").nth(0)).to_have_text("Test1.txt")
    expect(page.locator("#fileList").locator("li").nth(1)).to_have_text("Test2.txt")

    print("\n Files uploaded successfully.......")

    # Remove all selected files (clear input)
    page.locator("#filesToUpload").set_input_files([])

    # Validate cleared state
    expect(page.locator("#fileList li:nth-child(1)")).to_have_text("No Files Selected")

    page.wait_for_timeout(5000)
