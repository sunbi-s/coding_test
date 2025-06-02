import sys
from io import StringIO

# 테스트용 입력 예시
TEST_INPUT = """\
ObjectOrientedProgramming1 3.0 A+
IntroductiontoComputerEngineering 3.0 A+
ObjectOrientedProgramming2 3.0 A0
CreativeComputerEngineeringDesign 3.0 A+
AssemblyLanguage 3.0 A+
InternetProgramming 3.0 B0
ApplicationProgramminginJava 3.0 A0
SystemProgramming 3.0 B0
OperatingSystem 3.0 B0
WirelessCommunicationsandNetworking 3.0 C+
LogicCircuits 3.0 B0
DataStructure 4.0 A+
MicroprocessorApplication 3.0 B+
EmbeddedSoftware 3.0 C0
ComputerSecurity 3.0 D+
Database 3.0 C+
Algorithm 3.0 B0
CapstoneDesigninCSE 3.0 B+
CompilerDesign 3.0 D0
ProblemSolving 4.0 P
"""

# 로컬 테스트용 플래그
PYTHON_TEST = True

def main():
    count = 0
    score = 0.0
    for _ in range(20):
        name, credit, grade = sys.stdin.readline().split()
        print(name, credit, grade)  # 임시 확인
        credit = float(credit) 
        grade_dict={"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0.0, "P": None}
        if grade in grade_dict:
            grade = grade_dict[grade]
            if grade is not None:
                score += credit * grade
                count += credit
    print(round(score /count, 5))

if __name__ == "__main__":
    if "PYTHON_TEST" in globals():
        sys.stdin = StringIO(TEST_INPUT)
    main()
