import requests
import fake_useragent
from bs4 import BeautifulSoup

# 1000 28554
link = 'https://www.povarenok.ru/recipes/show/164365/'
response = requests.get(link)

# Забираем страницу и делаем преобразование в lxml, после чего сразу берем основной блок
soup = BeautifulSoup(response.text, 'lxml')
block = soup.find('article', class_='item-bl item-about')

# Название рецепта
name_recipe = block.find('h1', itemprop='name').text
print(name_recipe)

# Картинка
block_image = block.find('div', class_='m-img')
image_link = block_image.find('img').get('src')
image = requests.get(
    f'{image_link}').content  # придумать название для картинки, а также придумать как можно создавать папки
with open(f'image/{27}.jpg', 'wb') as file:
    file.write(image)

# Мини описание
descrip = block.find('div', class_='article-text')
text_des = descrip.find('p').text
print(text_des)

# Ингредиенты
ingr = block.find_all('h2')[0].text
print(ingr)

# Список ингредиентов
block_ingr = block.find('div', class_='ingredients-bl')
spisoc = block_ingr.find_all('li', itemprop='recipeIngredient')
a = []
for sp in spisoc:
    food = sp.find_all('span')
    if len(food) > 1:
        for i in range(len(food) - 1):
            a.append(f'{food[i].text} {food[i + 1].text}')
    else:
        a.append(f'{food[0].text}')  # В дальнейшем составить список и добавлять в основной список рецептов
print(a)


# Пошаговое описание (название)
step_name = block.find_all('h2')[-1].text
print(step_name)


# Пошаговое описание
# Функция удаления тегов
def delete_div(code, tag, arg):
    for div in code.find_all(tag, arg):
        div.decompose()


# Перечисление всех не нужных аргументов и последующее их удаление (сократить и добавить в цикл)
delete_div(block, 'span', '')
delete_div(block, 'td', '')
delete_div(block, 'tr', '')
delete_div(block, 'img', '')
delete_div(block, 'script', '')
delete_div(block, 'div', {'class': 'article-tags', 'id': 'tags-recipes-01'})
delete_div(block, 'div', {'class': 'ingredients-bl'})
delete_div(block, 'href', '')
delete_div(block, 'a', '')
delete_div(block, 'div', {'class': 'to-comments'})
delete_div(block, 'div', {'class': 'article-header'})
delete_div(block, 'div', {'class': 'user-info-main'})
delete_div(block, 'div', {'class': 'm-img'})
delete_div(block, 'div', {'class': 'article-text'})
delete_div(block, 'div', {'class': 'article-breadcrumbs'})
delete_div(block, 'h1', '')
delete_div(block, 'h2', '')
delete_div(block, 'div', {'itemprop': 'nutrition'})

step_desc = block.text.split()
step_desc_proc = ' '.join(step_desc)  # Полностью обработан и выводит в string, если нужен список, то .split()
print(step_desc_proc)


# cookies = {
#     '_ga': 'GA1.2.124709048.1709283988',
#     '_ga_CZGS1RJFZC': 'GS1.2.1709738451.6.0.1709738451.0.0.0',
#     'tmr_lvid': 'ec75f8924dfa9a56b277155edbbf3ed0',
#     'tmr_lvidTS': '1709284000139',
#     '_ym_uid': '170928400541376930',
#     '_ym_d': '1709284005',
#     'drs': '1',
#     '_gid': 'GA1.2.1813142692.1709738450',
#     '_gat': '1',
#     '_ym_isad': '2',
#     '_ym_visorc': 'b',
#     'tmr_detect': '0%7C1709738455086',
#     'gcmpoint': '1',
# }
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
#     'Accept-Language': 'en-US,en;q=0.5',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive',
#     'Cookie': '_ga=GA1.2.124709048.1709283988; _ga_CZGS1RJFZC=GS1.2.1709738451.6.0.1709738451.0.0.0; tmr_lvid=ec75f8924dfa9a56b277155edbbf3ed0; tmr_lvidTS=1709284000139; _ym_uid=170928400541376930; _ym_d=1709284005; drs=1; _gid=GA1.2.1813142692.1709738450; _gat=1; _ym_isad=2; _ym_visorc=b; tmr_detect=0%7C1709738455086; gcmpoint=1',
#     'Upgrade-Insecure-Requests': '1',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'none',
#     'Sec-Fetch-User': '?1',
# }
#
# response = requests.get('https://www.povarenok.ru/recipes/show/1000/', cookies=cookies, headers=headers).text
# print(response)
