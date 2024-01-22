from Topsis import __main__

input_file = "/Users/aditya/Desktop/6th_Sem/UCS654/102103546-data.csv"
output_file = "/Users/aditya/Desktop/6th_Sem/UCS654/102103546-result-2.csv"
weights = "1,1,1,1,1"
impacts = "+,+,-,+,-"

__main__.TOPSIS(input_file,weights,impacts,output_file)