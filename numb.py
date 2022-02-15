import selenium
from selenium import webdriver as wb
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys


web= wb.Chrome(r'C:\Users\Dell\Desktop\chromedriver.exe')
#web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes')
#web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:48&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:0&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')

time.sleep(5)
click = web.find_element_by_xpath(r'//*[@id="onetrust-accept-btn-handler"]')
time.sleep(5)
click.click()
dp_arr=[]
dp_arr2=[]
dp_arr3=[]
a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]
h=[]
img_arr =[]
count = 0
pr_id = []
for i in range(1,25):
    a.append(r'//*[@id="dijit__WidgetBase_1"]/li['+str(i)+']')
for i in range(1,25):
    b.append(r'//*[@id="dijit__WidgetBase_1"]/li['+str(i)+']')
for i in range(1,25):
    c.append(r'//*[@id="dijit__WidgetBase_2"]/li['+str(i)+']')
for i in range(1,25):
    d.append(r'//*[@id="dijit__WidgetBase_2"]/li['+str(i)+']')
for i in range(1,25):
    e.append(r'//*[@id="dijit__WidgetBase_2"]/li['+str(i)+']')
for i in range(1,25):
    f.append(r'//*[@id="dijit__WidgetBase_3"]/li['+str(i)+']')
for i in range(1,25):
    g.append(r'//*[@id="dijit__WidgetBase_4"]/li['+str(i)+']')
for i in range(1, 25):
    h.append(r'//*[@id="dijit__WidgetBase_5"]/li[' + str(i) + ']')


sample = []
arr = []
alldetails = []
url1 = []
df = pd.DataFrame()
temp = {'name of the product': '', 'product rating': '', 'product price': '', 'Product options': '', 'product image id': ''}
 #code has been modified. elif x==2 has been changed to if x==2 in order to scrape data frpom page 2. change it back to elif x==2
 #upon completion.

for x in range(0,7):
   if x==0:
      time.sleep(5)
      time.sleep(3)

      cli = web.find_element_by_class_name(r"product_listing_container")

      time.sleep(2)
      ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

      time.sleep(2)

      time.sleep(2)
      ele = ele.find_element_by_css_selector("ul")
      time.sleep(2)
      ele = ele.get_attribute(r'id')
      print(ele)
      cli =str(cli)
      for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li['+ str(i) +']')
      for i in range(0,24):
           cli = web.find_element_by_xpath(a[i])
           sample.append(cli.text)
      print(sample)
      for i in range(0,24):
          ele = web.find_element_by_xpath(a[count])
          ele = ele.find_element_by_id('catalogEntry_ID')
          ele = ele.get_attribute('value')
          ele = str(ele)
          ele= ele.replace(" ","")
          dp_arr.append(ele)
          count = count+1
      print(dp_arr)
      count =0
      for z in range(1, 25):
              url = r'//*[@id="dijit__WidgetBase_1"]/li['+str(z)+']'
              time.sleep(2)
              wb = web.find_element_by_xpath(url)
              time.sleep(1)
              img = wb.find_element_by_class_name(r'product_img')

              img = img.get_attribute("src")
              img_arr.append(img)
      print(img_arr)
      for i in range(0,len(dp_arr)):
          url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_'+dp_arr[i]+'_link_9b"]')
      print(url1)
      for z in sample:
          arr = z.split('\n')
          time.sleep(2)
          print(arr[0])
          cli = web.find_element_by_xpath(url1[count])
          time.sleep(6)
          time.sleep(5)
          print(cli)

          cli.click()

          time.sleep(5)
          cli2 = web.find_element_by_id(r'productId')
          pr_id.append(cli2.text)
          print(pr_id)

          temp.update({'name of the product': arr[0],'product rating': arr[1], 'product price': arr[2],'Product options': arr[3], 'product image id' : img_arr[count], 'product code':pr_id[count]})
          count = count +1
          df = df.append(temp, ignore_index=True)
          print(df)
          df.to_csv('thescrapereyelashes.csv')
          arr.clear()
          web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes')
      sample.clear()
      count =0
      url1.clear()
      dp_arr.clear()
   if x==1:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(b[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(b[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_1"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)
           temp.update({'name of the product': arr[0], 'product rating': arr[1], 'product price': arr[2],
                         'Product options': arr[3], 'product image id': img_arr[count], 'product code': pr_id[count]})
           count = count + 1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:24&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()
   if x==2:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(c[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(c[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_2"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)
           temp.update({'name of the product': arr[0], 'product rating': arr[1], 'product price': arr[2],
                         'Product options': arr[3], 'product image id': img_arr[count], 'product code': pr_id[count]})
           count = count + 1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:48&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()

   if x==3:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(d[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(d[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_2"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)
           temp.update({'name of the product': arr[0], 'product rating': arr[1], 'product price': arr[2],
                         'Product options': arr[3], 'product image id': img_arr[count], 'product code': pr_id[count]})
           count = count + 1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:72&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()

   if x==4:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(e[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(e[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_2"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)

           temp.update({'name of the product': arr[0],'product rating': arr[1], 'product price': arr[2],'Product options': arr[3], 'product image id' : img_arr[count], 'product code':pr_id[count]})
           count = count +1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:96&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()

   if x==5:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(f[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(f[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_3"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)
           temp.update({'name of the product': arr[0],'product rating': arr[1], 'product price': arr[2],'Product options': arr[3], 'product image id' : img_arr[count], 'product code':pr_id[count]})
           count = count +1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:120&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()

   if x==6:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(g[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(g[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_4"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)
           temp.update({'name of the product': arr[0],'product rating': arr[1], 'product price': arr[2],'Product options': arr[3], 'product image id' : img_arr[count], 'product code':pr_id[count]})
           count = count +1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:144&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()
   if x==7:
       time.sleep(5)
       time.sleep(3)

       cli = web.find_element_by_class_name(r"product_listing_container")

       time.sleep(2)
       ele = cli.find_element_by_class_name(r'plp_gridView_redesign')

       time.sleep(2)

       time.sleep(2)
       ele = ele.find_element_by_css_selector("ul")
       time.sleep(2)
       ele = ele.get_attribute(r'id')
       print(ele)
       cli = str(cli)
       for i in range(1, 25):
           a.append(r'//*[@id="' + ele + '"]' + r'/li[' + str(i) + ']')
       for i in range(0, 24):
           cli = web.find_element_by_xpath(h[i])
           sample.append(cli.text)
       print(sample)
       for i in range(0, 24):
           ele = web.find_element_by_xpath(h[count])
           ele = ele.find_element_by_id('catalogEntry_ID')
           ele = ele.get_attribute('value')
           ele = str(ele)
           ele = ele.replace(" ", "")
           dp_arr.append(ele)
           count = count + 1
       print(dp_arr)
       count = 0
       for z in range(1, 25):
           url = r'//*[@id="dijit__WidgetBase_5"]/li[' + str(z) + ']'
           time.sleep(2)
           wb = web.find_element_by_xpath(url)
           time.sleep(1)
           img = wb.find_element_by_class_name(r'product_img')

           img = img.get_attribute("src")
           img_arr.append(img)
       print(img_arr)
       for i in range(0, len(dp_arr)):
           url1.append(r'//*[@id="WC_CatalogEntryDBThumbnailDisplayJSPF_' + dp_arr[i] + '_link_9b"]')
       print(url1)
       for z in sample:
           arr = z.split('\n')
           time.sleep(2)
           print(arr[0])
           cli = web.find_element_by_xpath(url1[count])
           time.sleep(6)
           time.sleep(5)
           print(cli)

           cli.click()

           time.sleep(5)
           cli2 = web.find_element_by_id(r'productId')
           pr_id.append(cli2.text)
           print(pr_id)
           temp.update({'name of the product': arr[0],'product rating': arr[1], 'product price': arr[2],'Product options': arr[3], 'product image id' : img_arr[count], 'product code':pr_id[count]})
           count = count +1
           df = df.append(temp, ignore_index=True)
           print(df)
           df.to_csv('thescrapereyelashes.csv')
           arr.clear()
           web.get(r'https://www.boots.com/beauty/beauty-accessories/false-eyelashes#facet:&productBeginIndex:168&orderBy:&pageView:grid&minPrice:&maxPrice:&pageSize:&')
       sample.clear()
       count = 0
       url1.clear()
       dp_arr.clear()
   time.sleep(10)
   cli1 = web.find_element_by_xpath(r'//*[@id="WC_SearchBasedNavigationResults_pagination_link_right_categoryResults"]')
   time.sleep(2)
   cli1.click()