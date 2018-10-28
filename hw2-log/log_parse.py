# -*- encoding: utf-8 -*-

def insert(list, intKey):
    list[4] = list[3]
    list[3] = list[2]
    list[2] = list[1]
    list[1] = list[0]
    list[0] = intKey

def parse(
    ignore_files=False,
    ignore_urls=[],
    start_at=None,
    stop_at=None,
    request_type=None,
    ignore_www=False,
    slow_queries=False
):
    filename = 'log.log'

    checked_urls = {}
    checked_date = {}
    checked_type = {}
    checked_time = {}

    top_5_url = ['', '', '', '', '']
    top_5_url_count = [0, 0, 0, 0, 0]
    top_5_url_date = ['', '', '', '', '']
    top_5_url_type = ['', '', '', '', '']
    top_5_url_time = ['', '', '', '', '']

    with open(filename, 'r') as log_file:
        for line in log_file:
            if line[0] != '[':
                pass
            else:
                is_ok_for_parse = True

                list_of_data = line.split()
                
                request_date = list_of_data[0][1:] \
                             + ' ' \
                             + list_of_data[1][:-1]

                if (start_at != None) and (start_at > request_date): 
                    is_ok_for_parse = False

                if (stop_at != None) and (stop_at < request_date): 
                    is_ok_for_parse = False

                parsed_request_type = list_of_data[2][1:]

                if (request_type != None) and \
                        (request_type != parsed_request_type): 
                    is_ok_for_parse = False

                request = list_of_data[3]

                if (ignore_www == True) and ('www.' in request):
                    new_line = request.split('www.')
                    request = new_line[0] + new_line[1]

                protocol = list_of_data[4][:-1]

                response_code = list_of_data[5]

                response_time = list_of_data[6]

                if request in ignore_urls:
                    is_ok_for_parse = False

                if is_ok_for_parse:
                    if checked_urls.get(request) == None:
                        checked_urls[request] = 1
                        checked_date[request] = request_date
                        checked_type[request] = parsed_request_type
                        checked_time[request] = response_time
                    else:
                        checked_urls[request] += 1

                # if is_ok_for_parse:
                #     print('request_date:', request_date)
                #     print('request_type:', parsed_request_type)
                #     print('request:', request)
                #     print('protocol:', protocol)
                #     print('response_code:', response_code)
                #     print('response_time:', response_time)
                #     print()


    for key in  checked_urls:
        if checked_urls[key] >= top_5_url_count[0]:

            insert(top_5_url, key)

            insert(top_5_url_count, checked_urls[key])

            insert(top_5_url_date, checked_date[key])

            insert(top_5_url_type, checked_type[key])

            insert(top_5_url_time, checked_time[key])

    if slow_queries:
        summ_date = 0
        for i in range(0, len(top_5_url_time)):
            summ_date += int(top_5_url_time[i])
            middle = summ_date / len(top_5_url_time)
        print(middle // 1)

    for i in range(0, len(top_5_url)):
        print(
            top_5_url_count[i],
            top_5_url_date[i],
            top_5_url_type[i],
            top_5_url_time[i],
            '\n',
            top_5_url[i], end = '\n\n'
        )


        #print(checked_urls[key], ':', key)
    # print(top_5_url)
    # print(top_5_url_count)

parse(
    ignore_files=False,
    ignore_urls=[],
    start_at='28/Mar/2018 11:19:41',
    stop_at=None,
    # request_type='GET',
    #ignore_www=True,
    slow_queries=True
)

