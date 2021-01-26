import datetime

def spliceSpaceSeparatedStringIntoArray(string):
    result = []

    last_took_char_index = 0
    for char_index in range(0,len(string)):
        if char_index == len(string)-1:
            result.append(string[last_took_char_index:char_index])
        elif string[char_index] == " ":
            result.append(string[last_took_char_index:char_index])
            last_took_char_index = char_index+1

    return result

def readLinesAndCreateDictionary(raw_input):
    final_answers_to_print = {}

    num_of_testcases = int(raw_input.readline())    # num of testcases is the very first line
    for testcase_num in range(1,num_of_testcases+1):  # for each testcase, read the two lines and put them in the dictionary 
        
        testcase_meta_string = raw_input.readline()
        servers_cpus_string = raw_input.readline()
        testcase_meta_array = spliceSpaceSeparatedStringIntoArray(testcase_meta_string)
        servers_cpus_array = spliceSpaceSeparatedStringIntoArray(servers_cpus_string)
        
        final_answers_to_print[testcase_num] = {
            "goal_cpu": testcase_meta_array[1],
            "servers_cpus_array": servers_cpus_array,
        }

    return(final_answers_to_print)

def addAnotherServerCPUFromSequence(index_of_server,sum_of_cpu_power,goal_cpu,servers_cpu_array,smallestMarginOfPower,ending_index_of_final_sequence):
    sum_of_cpu_power += int(servers_cpu_array[index_of_server])
    # BASE CASE
    if sum_of_cpu_power >= goal_cpu:
        if sum_of_cpu_power-goal_cpu <= smallestMarginOfPower:
            smallestMarginOfPower = sum_of_cpu_power-goal_cpu
            return([index_of_server,ending_index_of_final_sequence, smallestMarginOfPower])
        else:
            return([])
    elif index_of_server-1 < 0:
        return([])
    return(addAnotherServerCPUFromSequence(index_of_server-1,sum_of_cpu_power,goal_cpu,servers_cpu_array,smallestMarginOfPower,ending_index_of_final_sequence))

def findFinalSequence(servers_cpu_array,goal_cpu):
    smallest_margin_of_power = 999999999999
    starting_index_of_final_sequence = 0
    ending_index_of_final_sequence = len(servers_cpu_array)

    for server_rack_cpu_id in reversed(range(0,len(servers_cpu_array))):
        result = addAnotherServerCPUFromSequence(server_rack_cpu_id,0,int(goal_cpu),servers_cpu_array,smallest_margin_of_power,server_rack_cpu_id)
        if len(result) > 2:
            starting_index_of_final_sequence = result[0]
            ending_index_of_final_sequence = result[1]
            smallest_margin_of_power = result[2]
    # When the loop above ends, we have the final server sequence
    return([starting_index_of_final_sequence,ending_index_of_final_sequence])

def main(raw_input,file_to_write_result):
    dict_of_testcases = readLinesAndCreateDictionary(raw_input)
    for key, testcase_data in dict_of_testcases.items():
        best_servers_sequence = findFinalSequence(testcase_data["servers_cpus_array"],testcase_data["goal_cpu"])
        final_message_to_print = "Case #"+str(key)+": "+str(best_servers_sequence[0])+" "+str(best_servers_sequence[1])
        file_to_write_result.write(final_message_to_print+"\n")
        
file_for_results = open("reply_result"+str(datetime.date.today())+".txt","w+")
inputs = open("input.txt", "r")
main(inputs,file_for_results)   
inputs.close()
file_for_results.close()