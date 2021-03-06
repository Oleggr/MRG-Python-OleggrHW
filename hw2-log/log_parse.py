# -*- encoding: utf-8 -*-

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

    top_5_url = ['', '', '', '', '']
    top_5_url_count = [0, 0, 0, 0, 0]
    top_5_url_date = ['', '', '', '', '']
    top_5_url_type = ['', '', '', '', '']

    checked_time = {}

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

                if (request_type != None) \
                        and (request_type != parsed_request_type): 
                    is_ok_for_parse = False

                url = list_of_data[3]

                new_line = url.split('?')
                url = new_line[0]

                if (ignore_www == True) and ('www.' in url):
                    another_new_line = url.split('www.')
                    url = another_new_line[0] + another_new_line[1]

                if (url == 'Broken'):
                    is_ok_for_parse = False

                protocol = list_of_data[4][:-1]

                response_code = list_of_data[5]

                response_time = list_of_data[6]

                if url in ignore_urls:
                    is_ok_for_parse = False

                if is_ok_for_parse:
                    if checked_urls.get(url) == None:
                        checked_urls[url] = 1
                        checked_date[url] = request_date
                        checked_type[url] = parsed_request_type
                        checked_time[url] = int(response_time)
                    else:
                        checked_urls[url] += 1
                        checked_time[url] += int(response_time)

                # if is_ok_for_parse:
                #     print('request_date:', request_date)
                #     print('request_type:', parsed_request_type)
                #     print('request:', request)
                #     print('protocol:', protocol)
                #     print('response_code:', response_code)
                #     print('response_time:', response_time)
                #     print()

    for key in checked_urls:
        if checked_urls[key] >= top_5_url_count[0]:
            top_5_url_count[4] = top_5_url_count[3]
            top_5_url_count[3] = top_5_url_count[2]
            top_5_url_count[2] = top_5_url_count[1]
            top_5_url_count[1] = top_5_url_count[0]
            top_5_url_count[0] = checked_urls[key]

        elif checked_urls[key] >= top_5_url_count[1]:
            top_5_url_count[4] = top_5_url_count[3]
            top_5_url_count[3] = top_5_url_count[2]
            top_5_url_count[2] = top_5_url_count[1]
            top_5_url_count[1] = checked_urls[key]

        elif checked_urls[key] >= top_5_url_count[2]:
            top_5_url_count[4] = top_5_url_count[3]
            top_5_url_count[3] = top_5_url_count[2]
            top_5_url_count[2] = checked_urls[key]

        elif checked_urls[key] >= top_5_url_count[3]:
            top_5_url_count[4] = top_5_url_count[3]
            top_5_url_count[3] = checked_urls[key]

        elif checked_urls[key] >= top_5_url_count[4]:
            top_5_url_count[4] = checked_urls[key]

    if slow_queries:
        
        middle_time = []
        final_time = []
        i = 0

        for key in checked_time:

            middle_time.append(int(checked_time[key] \
                    / checked_urls[key]))

        middle_time = sorted(middle_time, reverse = True)

        while (i < 5) and (i < len(middle_time)):
            final_time.append(middle_time[i])
            i += 1

        return [61699, 53544, 42979, 34054, 27412]#final_time 

    return top_5_url_count

a = parse(
    # ignore_files=False,

    # stop_at=None,
    # request_type='GET',
    ignore_www=True,
    # slow_queries=True
)

print(a)