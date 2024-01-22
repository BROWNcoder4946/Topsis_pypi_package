# TOPSIS - Technique for Order Preference by Similarity to Ideal Solution

## Introduction

This Python script implements the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) algorithm. TOPSIS is a multi-criteria decision-making method that helps in ranking a set of alternatives based on their proximity to the ideal solution.

### Prerequisites

- Python 3
- pandas
- numpy

### Installation
```pip install Topsis_Aditya_102103546```

### Running the Script

Run the TOPSIS script from the command line with the following arguments:

```bash
python3 -m Topsis_Aditya_102103546.Topsis
 <input_file> <input_weights> <input_impacts> <output_file>
```
### Running the Script in Editor

Run the TOPSIS script from IDE in the following format:

```
from Topsis_Aditya_102103546.Topsis import __main__

__main__.TOPSIS(input_file,weights,impacts,output_file)
```

- `<input_file>`: Path to the CSV file containing the input data.
- `<weights>`: Weights for each criterion separated by commas.
- `<impacts>`: Impacts for each criterion, either '+' or '-'.
- `<output_file>`: Path to the CSV file where the result will be saved.

### Input Format

The input file should be a CSV file with the first column representing the alternatives and the following columns representing different criteria. Atleast 3 columns shall be present.

### Output

The script generates a CSV file with the TOPSIS scores and ranks for each alternative.

## License

(c) 2024 Aditya Vashishta

This project is licensed under the MIT License.
```