#import re; print("challenge 1: ", sum([int(re.findall(r"\d+", result)[0])*int(re.findall(r"\d+", result)[1]) for result in re.findall(r"mul\(\d{1,3},\d{1,3}\)", open("./data/day3.txt", "r").read())])) # * challenge 1
import re;

#b = sum([int(re.findall(r"\d+", result[0])[0])*int(re.findall(r"\d+", result[1])[0]) for result in [re.findall(r"mul\(\d{1,3},\d{1,3}\)", i) for i in re.findall(r"(?:(?<=^)|(?<=do\(\))(?:(?!dont\(\)).)*?)mul\(\d{1,3},\d{1,3}\)", open("./data/day3.txt", "r").read())]])

with open("./data/test.txt", "r") as f:
    data = f.read()

step1 = re.findall(r"(?:(?<=^)|(?<=do\(\))(?:(?!don't\(\)).)*?)mul\(\d{1,3},\d{1,3}\)", data)
print(step1)

step2 = []
for step in step1:
    step2_step = re.findall(r"mul\(\d{1,3},\d{1,3}\)", step)[0]
    step2.append(step2_step)
print(step2)

step3 = []
for step in step2:
    step3_step = int(re.findall(r"\d+", step)[0]) * int(re.findall(r"\d+", step)[1])
    step3.append(step3_step)

step4 = sum(step3)

print(step4)

# a = sum([int(re.findall(r"\d+", mul)[0]) * int(re.findall(r"\d+", mul)[1]) for mul in [re.findall(r"mul\(\d{1,3},\d{1,3}\)", result)[0] for result in re.findall(r"(?:(?<=^)|(?<=do\(\))(?:(?!dont\(\)).)*?)mul\(\d{1,3},\d{1,3}\)", open("./data/day3.txt", "r").read())]])