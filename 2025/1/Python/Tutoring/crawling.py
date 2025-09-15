from playwright.sync_api import sync_playwright
import time
import json

start_time = time.time()

keyword = '홍대 맛집'
url = f'https://map.naver.com/p/search/{keyword}'
results = []

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    page.goto(url)

    page.wait_for_timeout(3000)  # 페이지 로딩 대기
    # searchIframe 진입
    page.wait_for_selector("iframe#searchIframe")
    search_frame = None
    for frame in page.frames:
        if frame.name == "searchIframe":
            search_frame = frame
            break
    if not search_frame:
        search_frame = page.frames[1]  # fallback

    for i in range(10):
        try:
            list_items = search_frame.query_selector_all("#_pcmap_list_scroll_container ul > li")
            if i >= len(list_items):
                print(f"[!] {i+1}번째 항목이 존재하지 않습니다.")
                break

            list_item = list_items[i]
            title_tag = list_item.query_selector(".CHC5F .bSoi3 .place_bluelink.N_KDL.CtW3e")
            if not title_tag:
                print(f"[!] {i+1}번째 항목 클릭 요소 없음")
                continue
            title_tag.scroll_into_view_if_needed()
            title_tag.click()
            page.wait_for_timeout(1000)

            # entryIframe 진입
            page.wait_for_selector("iframe#entryIframe")
            entry_frame = None
            for frame in page.frames:
                if frame.name == "entryIframe":
                    entry_frame = frame
                    break
            if not entry_frame:
                entry_frame = page.frames[-1]  # fallback

            main = entry_frame.query_selector("[role='main']")
            if not main:
                print(f"[!] {i+1}번째 main 요소 없음")
                continue

            # 이미지 추출
            img_urls = []
            try:
                image_sections = main.query_selector_all(".CB8aP > .uDR4i > .CEX4u")
                if image_sections and len(image_sections) > 0:
                    img = image_sections[0].query_selector(".fNygA > a > img")
                    if img:
                        img_urls.append(img.get_attribute("src"))
                if image_sections and len(image_sections) > 1:
                    divs = image_sections[1].query_selector_all(".hEm4D")
                    for div in divs:
                        for nest in div.query_selector_all(".CEX4u"):
                            img = nest.query_selector(".fNygA > a > img")
                            if img:
                                img_urls.append(img.get_attribute("src"))
            except Exception as e:
                pass

            # 타이틀, 카테고리 추출
            try:
                title_div = main.query_selector("#_title > div")
                title = title_div.query_selector(".GHAhO").inner_text() if title_div else ""
                category = title_div.query_selector(".lnJFt").inner_text() if title_div else ""
            except:
                title = category = ""

            print(f"{i+1}. title: {title}, category : {category}")

            # 메뉴 버튼 클릭
            try:
                menu_detail_btn = entry_frame.query_selector("//a[span[@class='veBoZ' and contains(text(), '메뉴')]]")
                if menu_detail_btn:
                    menu_detail_btn.click()
                    page.wait_for_timeout(500)
            except:
                pass

            # 메뉴 추출
            menus = []
            try:
                menu_list = entry_frame.query_selector_all("li.E2jtL")
                for menu in menu_list:
                    try:
                        menu_name = menu.query_selector("a.xPf1B > .MXkFw > .meDTN > .yQlqY > .lPzHi")
                        menu_desc = menu.query_selector("a.xPf1B > .MXkFw > .x.TRxGt > .kPogF")
                        menu_price = menu.query_selector("a.xPf1B > .MXkFw > .GXS1X > em")
                        menu_img = menu.query_selector("a.xPf1B > .YBmM2 > .place_thumb > img")
                        menus.append({
                            "name": menu_name.inner_text() if menu_name else "",
                            "desc": menu_desc.inner_text() if menu_desc else "",
                            "price": menu_price.inner_text() if menu_price else "",
                            "image": menu_img.get_attribute("src") if menu_img else ""
                        })
                    except:
                        continue
            except:
                pass

            results.append({
                "title": title,
                "category": category,
                "images": img_urls,
                "menus": menus
            })

        except Exception as e:
            print(f"[!] {i+1}번째 항목 처리 중 오류 발생: {e}")

end_time = time.time()
print(json.dumps(results, ensure_ascii=False, indent=4))
print(f"Execution time: {end_time - start_time:.2f} seconds")