instructions_orig = [3,225,
1,225,6,6,
1100,1,238,225,104,0,1101,82,10,225,101,94,44,224,101,-165,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,35,77,225,1102,28,71,225,1102,16,36,225,102,51,196,224,101,-3468,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1001,48,21,224,101,-57,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,2,188,40,224,1001,224,-5390,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,9,32,224,101,-41,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1102,66,70,225,1002,191,28,224,101,-868,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1,14,140,224,101,-80,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1102,79,70,225,1101,31,65,225,1101,11,68,225,1102,20,32,224,101,-640,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,1002,223,2,223,1006,224,329,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,404,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,464,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226]
cur_pos = 0
instructions = instructions_orig.copy()
while instructions[cur_pos] != 99:
    method = instructions[cur_pos] % 100
    if method == 3:
      val = input("Enter mode 3 input: ")
      instructions[instructions[cur_pos + 1]] = int(val)
      cur_pos += 2
    elif method == 4:
      print("Mode 4 output: " + str(instructions[instructions[cur_pos + 1]]))
      cur_pos += 2
    else:
      param1_mode = (instructions[cur_pos] - method) % 1000
      param2_mode = (instructions[cur_pos] - method - param1_mode) % 10000
      pos_1 = instructions[cur_pos + 1] if param1_mode == 0 else cur_pos + 1
      pos_2 = instructions[cur_pos + 2] if param2_mode == 0 else cur_pos + 2
      if method == 5:
        cur_pos = instructions[pos_2] if instructions[pos_1] != 0 else cur_pos + 3
      elif method == 6:
        cur_pos = instructions[pos_2] if instructions[pos_1] == 0 else cur_pos + 3
      else:
        param3_mode = (instructions[cur_pos] - method - param1_mode - param2_mode) % 100000
        pos_3 = instructions[cur_pos + 3] if param3_mode == 0 else cur_pos + 3
        if method == 1:
          instructions[pos_3] = instructions[pos_1] + instructions[pos_2]
        elif method == 2:
          instructions[pos_3] = instructions[pos_1] * instructions[pos_2]
        elif method == 7:
          instructions[pos_3] = 1 if instructions[pos_1] < instructions[pos_2] else 0
        elif method == 8:
          instructions[pos_3] = 1 if instructions[pos_1] == instructions[pos_2] else 0
        cur_pos += 4
