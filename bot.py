import asyncio
from playwright.async_api import async_playwright, TimeoutError

ANSWER = "B"

accounts = [




{"username": "HC-51", "wallet": "XEGW1JHY7Y6dzo1G2LiwbPZjGjF9Kn2GK5FN5RhpHx3"},
{"username": "HC-52", "wallet": "9fw34BiMaR3f2eC2uBFiSSUU37QtBDSJfKFWBxWW1T2d"},
{"username": "HC-53", "wallet": "E4FkMmn8KBKrtbRqBgL22tkcQAWHSPApWQ1Azqua9ud1"},
{"username": "HC-54", "wallet": "CkYeq87JU6NzLCXbggKimbbaaYf3EED9woNNqCSeVt1Z"},
{"username": "HC-55", "wallet": "Bf6Zn7cWTBiSt85neZUCojeUDNTAbhxNTmCSWGa784tH"},
{"username": "HC-56", "wallet": "DaA7UFNhmS5nwfxHvrNiYVqyiGWF2FyoQmhT2j22aLYS"},
{"username": "HC-57", "wallet": "HoActUhW9CyHdyDoFXrCddGqUwg87yW4bZD7w4NjXErg"},
{"username": "HC-58", "wallet": "7kYYr4f2Gx52YKVP3qrBqocCUh3bSLCWAha3qHwCF4tw"},
{"username": "HC-59", "wallet": "87BUGmzxhQpBXoaLdgdQvYtYHygpvgbbWppdKXjfRNtj"},
{"username": "HC-60", "wallet": "6LsBNMPFRMUx6hph7osQdBkbBhpsXEen8pM1LnqWVvwY"},
{"username": "HC-61", "wallet": "Hq4Amw9qdHAB6w55zaGYKpkUxri9qFJXC1nUeTGvJJrf"},
{"username": "HC-62", "wallet": "FeEYv6BjAtDhmLQD1fG2nL7MmyXyyfcvtnSNsq3UWKgX"},
{"username": "HC-63", "wallet": "BLV55XiifDPBkmXUtmjBX7sbfLM7r7j494WohBjQApT3"},
{"username": "HC-64", "wallet": "DMx5o5K9Ccpzd1MRfy8d1U5uoceAxfiBYUu6Esr8x6YM"},
{"username": "HC-65", "wallet": "7o5v1UX5C9H1SjbnHQGTQPkHcgo1TYpp6FKp9U5oRFXW"},
{"username": "HC-66", "wallet": "Ec8qCVBgncS7dfjExfMxZwRuuGnBmA456PLyzsMaBTEg"},
{"username": "HC-67", "wallet": "FXaXDJTwfaesc5R6cRQMq4MeQW2kdJnqymmtLnXBNYK"},
{"username": "HC-68", "wallet": "DDgBh8huEzGrGmqm9Vqq4q52E48DyZFnsjTavMMwmXo3"},
{"username": "HC-69", "wallet": "2wMcArWLL8sQuv3va61Ahp69eVNozqrLo8yvMXNqoEuZ"},
{"username": "HC-70", "wallet": "2WUUm8qEEA4MRg1LWtkq9riVBUuH87qsRoJLm5rGFkuV"},
{"username": "HC-71", "wallet": "DVtXQgWdaShET9YDhrZwGk7da47ebiDFb1wwgyresmdz"},
{"username": "HC-72", "wallet": "5c4audp62kq7jBf1RT6YcM2UVGeKfEF6iAbsWbVNdYQg"},
{"username": "HC-73", "wallet": "8yg33wwgZ2J8pGPi9RGMU4v9gYChZswWdYSsY6KAdgZZ"},
{"username": "HC-74", "wallet": "F6MvgEEnapq9c6n4UZg9j1UNfbcC4NXsANcMbd6ebj6T"},
{"username": "HC-75", "wallet": "5Rq2RbuBr1tk5bge6KeGVENjpBqLrcYkDKaV4J7rzhmz"},
{"username": "HC-76", "wallet": "7tqpKUVv2cKfJvaisKoyjAcukhxmvZ1gj6epr3q928xq"},
{"username": "HC-77", "wallet": "4Vtim5fHq1KBpkKNdLBFLeqNK3kGaSiV36QDrAUaLT6g"},
{"username": "HC-78", "wallet": "8QSrgKkk93auu51pdjUKVRyg9oaEAWDQVugarjbckNZe"},
{"username": "HC-79", "wallet": "HpMcs6Gv32pxifvUJkCkRfWx1NRiRkoFEsqMtd64GodT"},
{"username": "HC-80", "wallet": "2eBtGMUTWQ2sR8a96YKB6vc3F4CnfbQdZxx87p3B5jSF"},
{"username": "HC-81", "wallet": "GfuzKs8G3uf6FiTui4Qe27RaQ4mHwHb9BXyiwJMjhCZ3"},
{"username": "HC-82", "wallet": "H289fKRt431uyUacC79FxmE1URb8jE9qHdtZNggT16dy"},
{"username": "HC-83", "wallet": "8cKkHyxbHQgV5tXoYeXHY3756pMFNmSRgmmRu6hEb5SG"},
{"username": "HC-84", "wallet": "A2ZcLyZJ97HKTpnsbAuAUbsqVZxjqaUx3MwwjnxkLVFM"},
{"username": "HC-85", "wallet": "4Koyff6CqGB8HSpKpPaaLBZLdXaVUbfn1GpwJGoPW28s"},
{"username": "HC-86", "wallet": "6ipyFPeBXuiyHKxQHqUPNWcj9qCaCKykPsxmxxTVGeoe"},
{"username": "HC-87", "wallet": "C6bkcD1U2GZJ9bPN25jHbD1CCc94nWcC31JwMLSq8cgL"},
{"username": "HC-88", "wallet": "2bu6X19Se9P8o6CiWNiyaSzJnv9bSkz1WnmvHQZa9Mfs"},
{"username": "HC-89", "wallet": "Fd9y12y7krfyPPuA3AAgY9WajyMobj88XRwjJbotiaqf"},
{"username": "HC-90", "wallet": "Drn9fo9vKQViS3NimDVyENYhpGLMUAnkJPEqiYeg8k8q"},
{"username": "HC-91", "wallet": "61TBFU21hZ8y7nEdAX6CUhQZMnbzJZz9kpoXHYS6pmHM"},
{"username": "HC-92", "wallet": "Go7CSFaRVLvWUbniuwoDxpWTT9joZaUgez9N2vpCg9HP"},
{"username": "HC-93", "wallet": "HLTsKkSsYK1aU4jKxU5x4xiKkcmuqNxNT5Z4t6NxHG7S"},
{"username": "HC-94", "wallet": "5oMVchhNEARpmCyHy411viMjDdP1Ny1tmdbX3R8YEmTp"},
{"username": "HC-95", "wallet": "4cN1hG4yJcQk61uQzzwkiVKjt14LdwL2tpTiBc6bwvKG"},
{"username": "HC-96", "wallet": "DBjK3SZY4GZnrBNW5LgTgGDkyK5kaWoB5Ri4E7b4LTxk"},
{"username": "HC-97", "wallet": "A8vyxq9A7ELqEBjXK4Pa6MHMS6Pv3Zr7fyX4iwqWkdMD"},
{"username": "HC-98", "wallet": "EigWRSmjjeY3ZsJ9GuM3NBe2VdEEStVR5gUrdXDskuJU"},
{"username": "HC-99", "wallet": "CTwbFhxxYsJS4cyVkqB7iEb5fCyePVf1MKdASFUrsQgP"},
{"username": "HC-100", "wallet": "7Rqx8TAVc9caD1T6vUznto5MG9Z3M74ZDahsUPREuhER"},




   
]

async def handle_modal(page):
    modal = page.locator("#scamMigrationWarningModal")
    try:
        if await modal.is_visible(timeout=5000):
            print("⚠️ Closing modal...")
            buttons = modal.locator("button")
            if await buttons.count() > 0:
                await buttons.first.click()
                await page.wait_for_timeout(1000)
    except:
        pass

async def run_bot():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        for acc in accounts:
            context = await browser.new_context()
            page = await context.new_page()

            print("Running account:", acc["username"])

            try:
                await page.goto("https://theros.io/prelaunch", timeout=80000)
                await page.wait_for_load_state("networkidle", timeout=15000)
            except TimeoutError:
                print(f"Timeout for {acc['username']}. Skipping.")
                await context.close()
                continue

            await handle_modal(page)
            await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
            await page.wait_for_selector("input", timeout=15000)

            inputs = await page.query_selector_all("input")
            if len(inputs) < 2:
                print(f"Not enough inputs for {acc['username']}, skipping")
                await context.close()
                continue

            await inputs[0].fill(acc["username"])
            await inputs[1].fill(acc["wallet"])

            if len(inputs) > 2:
                await inputs[2].fill("bot")

            await handle_modal(page)

            create_btn = page.locator("#registerBtn")
            try:
                await create_btn.click(timeout=9000)
            except TimeoutError:
                await create_btn.click(force=True)

            next_btn = page.locator("#nextQuestionBtn")
            try:
                await next_btn.wait_for(state="visible", timeout=8000)
                await next_btn.click()
            except:
                pass

            answer_selector = f"#answer{ANSWER.upper()}"
            try:
                await page.locator(answer_selector).click(timeout=20000)
                print("Answered:", ANSWER)
            except Exception as e:
                print(f"Failed to answer: {e}")

            await page.wait_for_timeout(1000)
            await context.close()

        await browser.close()
        print("🎉 All accounts processed successfully!")

if __name__ == "__main__":
    asyncio.run(run_bot())
