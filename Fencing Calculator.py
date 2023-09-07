# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 01:09:17 2023

@author: wlowery
"""

import os
import win32gui
import time

rb_link = 'https://www.lowes.com/pd/Severe-Weather-Common-5-4-in-x-6-in-x-8-ft-Actual-1-in-x-5-5-in-x-8-ft-Standard-Treated-Lumber/4564780'

fp_link = 'https://www.lowes.com/pd/Severe-Weather-Common-4-in-x-4-in-x-8-ft-Actual-3-5-in-x-3-5-in-x-8-ft-2-Treated-Lumber/50121083'

bc_link = 'https://www.lowes.com/pd/QUIKRETE-50-lb-Fast-Setting-Concrete-Mix/3006121'

txfr_link = 'https://www.lowes.com/pd/Severe-Weather-Common-2-in-x-4-in-x-8-ft-Actual-1-5-in-x-3-5-in-x-8-ft-2-Prime-Treated-Lumber/4564608'

p_link = 'https://www.lowes.com/pd/Severe-Weather-5-8-in-x-5-1-2-in-x-6-ft-Pressure-Treated-Southern-Yellow-Pine-Dog-Ear-Fence-Picket/5013086547'

sn_link = 'https://www.lowes.com/pd/Metabo-HPT-was-Hitachi-Power-Tools-2-Inch-Full-Round-Head-Wire-Coil-Siding-Nail-Metabo-HPT-13365HHPT/5003123569'

fn_link = 'https://www.lowes.com/pd/Hitachi-3-Inch-21-Degree-Pneumatic-Nails-Metabo-HPT-20302SHPT/5001960993'

webmats = {'rot_boards_price': rb_link, 'fence_posts_price': fp_link,
           'bags_cement_price': bc_link, 'twoxfour_rails_price': txfr_link,
           'pickets_price': p_link, 'siding_nails_price': sn_link,
           'framing_nails_price': fn_link}

webmats_vals_list = list(webmats.values())

static_text_elements = ['7.48', '10.88', '6.71', '5.38', '2.18', '97.98', '49.98']  # Adjust the tag selection based on the page structure

staticmats = {'rot_boards_price': '7.48', 'fence_posts_price': '10.88',
              'bags_cement_price': '6.71', 'twoxfour_rails_price': '5.38',
              'pickets_price': '2.18', 'siding_nails_price': '97.98',
              'framing_nails_price': '49.98'}

staticmats_list = list(staticmats)
staticmats_vals_list = list(staticmats.values())

mats = {}

def loading_message():
    
    lm = '.'
    for x in range(3):
        print(lm, end='')
        time.sleep(.5)
    return ''

def zorro_title(): 
                                     
    print('\n\n\n\n\n\n\n'\
          '\t\t                  ^7?J.                                    ::.^~         ~~     .       \n'\
          '\t\t     ..           .:^:    !P5J~: ...                  .!JYJ#&#@@Y~!      ..     !PJ?J^.\n'\
          '\t\t  :~JB#5.                !&@@@@&GGJ:                  5P&@@@@@@@@@7         :. ?@@@@@B~\n'\
          '\t\t :G@@@@@5.              7@@@&G?!^^.                      .^?YP#@@#?^        .^J@@@@#Y.\n'\
          '\t\t   .^75B#@G!         :~JGBPY!:                                 :~!^^      :JPB&G5J!.  \n'\
          '\t\t         .:^^         !7!:.                                             .^::.       \n'\
          '\t\t                                                                                    \n'\
          '\t\t                                                                                  \n'\
          '\t\t                                                                                      ')
    
    time.sleep(2)
        
    os.system('cls')
    
    time.sleep(.5)
    
    print('\n\n\n\n\n\n\n\t\t\t\t\t\t   Zօɾɾօ Technօlօgies™')
    return ''

def GetElementsActive(x):
    
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from bs4 import BeautifulSoup

    def GetChromedriverPath(path):
        
        def scrape_driver_txt(val):
            for x in range(9):
                place = file.readline()
            return place

        this_dir, this_filename = os.path.split(__file__)

        my_txt = os.path.join(this_dir, 'uChromedriverPath.txt')

        file = open(my_txt, 'r')
        
        uChromedriverPath = scrape_driver_txt('').replace('>', '').replace('<', '').replace('C', 'c')

        return uChromedriverPath

    chrome_key = (str(GetChromedriverPath('')))
    
    chromedriver_path = chrome_key.replace('\n', '')

    # URL to scrape
    url = str(x)

    # Set up Chrome driver
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service)
    driver.get(url)

    # Wait for the page to load (adjust the wait time as needed)
    driver.implicitly_wait(10)

    # Get the page source after JavaScript rendering
    page_source = driver.page_source

    # Close the driver
    driver.quit()

    # Parse the page source with BeautifulSoup
    soup = BeautifulSoup(page_source, 'html.parser')

    # Find and print the text content
    text_elements = soup.find_all('span', class_='screen-reader')  # Adjust the tag selection based on the page structure

    global mats
    
    for element in text_elements:
        price = element.get_text()
        global clean_price
        clean_price = float(price.replace('$', '').strip())
        return clean_price
        break

def GetElementsStatic(x):
    
    for element in static_text_elements:
        price = element
        global clean_price
        clean_price = float(price.replace('$', '').strip())
        return clean_price

def round_up(number): 
    
    return int(float(number) + float(float(number) % 1.00 > 0.00))

def UnitCalculator():
    
    control_var = 1
    
    while(control_var != 0):
        
        try:
            
            if control_var == 1:
            
                fence_length = int(round_up(input('\nTo create a cost estimate, input the desired '\
                                                  'length of fence in linear feet '\
                                                      'then press ENTER\n\n')))
                control_var = 0
            
            else:
                
                fence_length = int(round_up(input('\nInput the desired length of fence in linear feet '\
                                                      'then press ENTER\n\n')))
                control_var = 0
                    
        except:
            
            print('\nOops! User input must be entered using numeric values only. '\
                  'Examples of valid entries include: '\
                  '\n\n100\n\n100.75 ')
                
            time.sleep(5)
            os.system('cls')
            
            pass
        
    print('\nFor ' + str(fence_length) + ' linear feet of fencing, the estimated cost equals:')
    
    time.sleep(1)
    
    print(loading_message())
    
    val_fence_sections = round_up(fence_length / 7)
    
    x = val_fence_sections
    
    val_rot_boards = float(x)
    
    val_fence_posts = float(x + 1)
    
    val_bags_cement = float(x + 1)
    
    val_twoxfour_rails = float(x * 3)
    
    val_pickets = float(x * 16)
    
    val_siding_nails = float(x * 100)
    
    val_framing_nails = float(x * 20)
    
    global units
    
    units = {'rot_boards': val_rot_boards,
             'fence_posts': val_fence_posts, 'bags_cement': val_bags_cement,
             'twoxfour_rails': val_twoxfour_rails, 'pickets': val_pickets,
             'siding_nails': val_siding_nails, 'framing_nails': val_framing_nails}
    
    #strings = [float(x) for x in units.values()]

def CostCalculator():
    
    global units
    global current_mats
    global cost_dictionary
    global per_cost_dictionary
    global total_all
    
    rot_boards_per = current_mats.get('rot_boards_price')
    
    fence_posts_per = current_mats.get('fence_posts_price')
    
    bags_cement_per = current_mats.get('bags_cement_price')
    
    twoxfour_rails_per = current_mats.get('twoxfour_rails_price')
    
    pickets_per = current_mats.get('pickets_price')
    
    siding_nails_per = (float(current_mats.get('siding_nails_price')) / 3600.00)
    
    framing_nails_per = (float(current_mats.get('framing_nails_price')) / 1000.00)
    
    
    rot_boards_total = units.get('rot_boards') * float(rot_boards_per)
    
    fence_posts_total = units.get('fence_posts') * float(fence_posts_per)
    
    bags_cement_total = units.get('bags_cement') * float(bags_cement_per)
    
    twoxfour_rails_total = units.get('twoxfour_rails') * float(twoxfour_rails_per)
    
    pickets_total = units.get('pickets') * float(pickets_per)
    
    siding_nails_total = units.get('siding_nails') * float(siding_nails_per)
    
    framing_nails_total = units.get('framing_nails') * float(framing_nails_per)
    
    
    total_all = "{:.2f}".format(float(rot_boards_total) + float(fence_posts_total) + float(bags_cement_total) + 
                 float(twoxfour_rails_total) + float(pickets_total) + float(siding_nails_total) +
                 float(framing_nails_total))
    
    
    per_cost_dictionary = {'rot_boards_per_key': rot_boards_per, 'fence_posts_per_key':
                            fence_posts_per, 'bags_cement_per_key': bags_cement_per,
                            'twoxfour_rails_per_key': twoxfour_rails_per, 'pickets_per_key':
                                pickets_per, 'siding_nails_per_key': siding_nails_per,
                                'framing_nails_per_key': framing_nails_per}

    cost_dictionary = {'rot_boards_total_key': rot_boards_total, 'fence_posts_total_key':
                       fence_posts_total, 'bags_cement_total_key': bags_cement_total,
                       'twoxfour_rails_total_key': twoxfour_rails_total, 'pickets_total_key':
                           pickets_total, 'siding_nails_total_key': siding_nails_total,
                           'framing_nails_total_key': framing_nails_total}

def line_break(val):
    
    linebreak = ''
    for x in range(val):
        linebreak += '*'
    return linebreak

def leading_whitespace(val):

    whitespace = ''
    for x  in range((48 - len(val))):
        whitespace += ' '
    return whitespace
        
def trailing_whitespace():
    global raw_receipt_line
    
    whitespace = ''
    for x  in range((48 - len(raw_receipt_line))):
        whitespace += ' '
    return whitespace

def receipt(val1, val2, val3, val4):
    stab = '   '
    xstab = ' '
    usd = '$'
    unit_name = val4
    unit_quantity = str(int(val1))
    
    if float(val2) >= 1.00:
        unit_price = "{:.2f}".format(float(val2))
    else:
        unit_price = "{:.4f}".format(float(val2))
    
    unit_cost = "{:.2f}".format(float(val3))
    
    
    global raw_receipt_line
    raw_receipt_line = ("{} {}{}ea{}@{}1/{}{}{}{}{}{}".format(unit_name, unit_quantity, stab, xstab, stab, 
                                                           xstab, usd, unit_price, '', usd, unit_cost))
    
    white = trailing_whitespace()
            
    current_receipt_line = ("\n{} {}{}ea{}@{}1/{}{}{}{}{}{}".format(unit_name, unit_quantity, stab, xstab, stab, 
                                                        xstab, usd, unit_price, white,
                                                        usd, unit_cost))
    print(current_receipt_line)
    
    return ''

class MaterialClass:
    
    def __init__(self, unit_quantity, unit_price, unit_cost):
        
        self.__unit_quantity = unit_quantity
        self.__unit_price = unit_price
        self.__unit_cost = unit_cost
        
    def set_quantity(self, unit_quantity):
        self.__unit_quantity = unit_quantity
            
    def set_unit_price(self, unit_price):
        self.__unit_price = unit_price

    def set_total_price(self, unit_cost):
        self.__unit_cost = unit_cost
                
    def get_quantity(self):
        return self.__quantity
        
    def get_unit_price(self):
        return self.__unit_price
        
    def get_total_price(self):
        return self.__total_price

if __name__ =='__main__':
    
    win32gui.SetWindowText(win32gui.GetForegroundWindow(), 'Fencing Calculator v1.0a')
    
    program = 'running'
    
    print(zorro_title())
    time.sleep(3)
    os.system('cls')
    
    print('\nFetching live pricing data, all materials\n\n'\
              'Please do not close or interrupt your web browser')
    time.sleep(1)
    
    print(loading_message())
    time.sleep(1)
    
    os.system('cls')
    
    try:
        
        for x in webmats_vals_list:
            node_count = webmats_vals_list.index(x)
            webmats_keys_list = list(webmats.keys())
            current_price = GetElementsActive(x)
        
            os.system('cls')
        
            mats[(webmats_keys_list[node_count])] = current_price
            
            current_mats = mats
            
    except:
        
        control_var = 1
        
        while(control_var == 1):
            
            try:
                
                os.system('cls')
                
                user_choice = input('\nOops! This program encountered an issue '\
                                    'while fetching your data\n\nIf you would '\
                                    'like to attempt data retrieval one more time, '\
                                    'please press ENTER\n\nTo continue with '\
                                    'generic pricing data, type \"exit\" then press ENTER\n\n')
                
                if user_choice.lower() == 'exit':
                
                    control_var = 0
                    
                    for x in staticmats_vals_list:
                        node_count = (staticmats_vals_list.index(x))
                        staticmats_keys_list = list(staticmats.keys())
                        current_price = GetElementsStatic(x)
                        
                        current_price = x
                    
                        os.system('cls')
                    
                        mats[(webmats_keys_list[node_count])] = current_price
                    
                        current_mats = mats
                 
                else:
                    
                    for x in webmats_vals_list:
                        node_count = webmats_vals_list.index(x)
                        webmats_keys_list = list(webmats.keys())
                        current_price = GetElementsActive(x)
                    
                        os.system('cls')
                    
                        mats[(webmats_keys_list[node_count])] = current_price
                        
                        current_mats = mats
                    
            except:
                    
                pass
    
    global cost_dictionary
    global per_cost_dictionary
    global total_all
    
    while(program.lower() != 'exit'):
        
        UnitCalculator()
        CostCalculator()
    
        units_vals_list = list(units.values())
        per_cost_dictionary_list = list(per_cost_dictionary.values())
        cost_dict_vals_list = list(cost_dictionary.values())
        units_keys_list = list(units.keys())
    
        node1_count = 0
    
        for x in range(len(webmats_vals_list)):
            newlist = [(units_vals_list[node1_count]),
                       (per_cost_dictionary_list[node1_count]),
                       (cost_dict_vals_list[node1_count]),
                       (units_keys_list[node1_count])]
            print(receipt(*newlist))
            node1_count += 1
       
        raw_subtotal = ('$' + str(total_all))
        raw_sales_tax = ('$' + "{:.2f}".format(float(total_all) * 0.0825))
        raw_total_sale = ('$' + "{:.2f}".format(float(total_all) * 1.0825))
        
        subtotal_white = leading_whitespace('subtotal' + str(raw_subtotal))
        sales_tax_white = leading_whitespace('sales_tax' + str(raw_sales_tax))
        total_sale_white =  leading_whitespace('total_sale' + str(raw_total_sale))
        
        subtotal = ("subtotal{}{}".format(subtotal_white, raw_subtotal))
        sales_tax = ("sales_tax{}{}".format(sales_tax_white, raw_sales_tax))
        total_sale = ("total_sale{}{}".format(total_sale_white, raw_total_sale))
        
        print(line_break(48) + '\n\n' + 
              subtotal + '\n\n' + str(sales_tax) + '\n\n')
        
        print(line_break(48) + '\n\n' + 
              str(total_sale))
        
        program = str(input('\nPress ENTER to continue\n'))
        
    #qt = units.get('rot_boards')
    # up = current_mats.get('rot_boards_price')
    #tp = cost_dictionary.get('rot_boards_total_key')

    #RotBoards = MaterialClass(qt, up, tp)

    #print(f'\nThank you for designating your object\'s attributes!\n\
    #      \nHere are the current stats for your object:\
    #      \nquantity = {RotBoards.get_quantity()}')
    
    #'fence_sections': val_fence_sections, 