import urllib.request
import re
import csv
import time
import random

def get_fund_companies(page_num=1):
    url = f"https://fund.eastmoney.com/company/default.html?page={page_num}&sortType=allScale&sortDirect=desc&feType=all&letter="
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Referer": "https://fund.eastmoney.com/company/default.html"
    }
    
    try:
        print(f"正在请求 URL: {url}")
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=15) as response:
            html = response.read().decode("utf-8")
        
        print(f"HTML长度: {len(html)}")
        
        pattern = r'<tr class="(?:grey-bg)?">.*?</tr>'
        rows = re.findall(pattern, html, re.DOTALL)
        print(f"找到 {len(rows)} 行数据")
        
        if len(rows) > 0:
            print("第一行示例:")
            print(rows[0][:500])
        
        companies = []
        
        for row in rows:
            company = {}
            
            sno_match = re.search(r'<td class="sno width50">(\d+)</td>', row)
            if sno_match:
                company["序号"] = sno_match.group(1)
            else:
                continue
            
            name_match = re.search(r'<td class="td-align-left".*?><a href="([^"]+)">([^<]+)</a></td>', row)
            if name_match:
                company["基金公司名称"] = name_match.group(2)
                href = name_match.group(1)
                if href.startswith("http"):
                    company["基金公司链接"] = href
                else:
                    company["基金公司链接"] = "https://fund.eastmoney.com" + href
            
            create_time_match = re.search(r'<td>(\d{4}-\d{2}-\d{2})</td>', row)
            if create_time_match:
                company["成立时间"] = create_time_match.group(1)
            
            rating_stars = len(re.findall(r'<label class="sprite sprite-star5"></label>', row))
            company["天项评级"] = f"{rating_stars}星"
            
            scale_match = re.search(r'<p class="td-gm">([\d,]+(?:\.\d+)?)\s*&nbsp;', row)
            if scale_match:
                company["全部管理规模"] = scale_match.group(1)
            
            fund_num_match = re.search(r'<td><a href="[^"]+">(\d+)</a></td>', row)
            if fund_num_match:
                company["全部基金数"] = fund_num_match.group(1)
            
            manager_num_match = re.search(r'<td><a href="[^"]+jjjl_[^"]+">(\d+)</a></td>', row)
            if manager_num_match:
                company["全部经理数"] = manager_num_match.group(1)
            
            if company.get("序号") and company.get("基金公司名称"):
                companies.append(company)
        
        print(f"解析出 {len(companies)} 条公司数据")
        return companies
    except Exception as e:
        print(f"获取第 {page_num} 页数据失败: {str(e)}")
        return []

def main():
    all_companies = []
    page_num = 1
    
    print("开始爬取基金公司排名数据...")
    
    companies = get_fund_companies(page_num)
    print(f"第 {page_num} 页获取到 {len(companies)} 条数据")
    
    if companies:
        print("第一条数据示例:")
        print(companies[0])
    
    all_companies.extend(companies)
    
    print(f"\n爬取完成，共获取 {len(all_companies)} 条基金公司数据")
    
    if all_companies:
        output_file = "fund_companies.csv"
        with open(output_file, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=["序号", "基金公司名称", "基金公司链接", "成立时间", "天项评级", "全部管理规模", "全部基金数", "全部经理数"])
            writer.writeheader()
            for company in all_companies:
                row = {
                    "序号": company.get("序号", ""),
                    "基金公司名称": company.get("基金公司名称", ""),
                    "基金公司链接": company.get("基金公司链接", ""),
                    "成立时间": company.get("成立时间", ""),
                    "天项评级": company.get("天项评级", ""),
                    "全部管理规模": company.get("全部管理规模", ""),
                    "全部基金数": company.get("全部基金数", ""),
                    "全部经理数": company.get("全部经理数", "")
                }
                writer.writerow(row)
        
        print(f"数据已保存到 {output_file}")
    else:
        print("未获取到任何数据")

if __name__ == "__main__":
    main()