def hanoi_solver(number_of_disks):
    peg_arr = {
        'peg_left': list(range(number_of_disks, 0, - 1)),
        'peg_mid': [],
        'peg_right': []
    }
    moves = []
    moves.append(f'{peg_arr["peg_left"]} {peg_arr["peg_mid"]} {peg_arr["peg_right"]}')
    
    def solve_move(n, source, target, helper):
        if n == 1:
            disk_movement = source.pop()
            target.append(disk_movement)
            moves.append(f'{peg_arr["peg_left"]} {peg_arr["peg_mid"]} {peg_arr["peg_right"]}')
            

        if n > 1:
            result = solve_move(n - 1, source, helper, target)
            
            disk_movement = source.pop()
            target.append(disk_movement)
            moves.append(f'{peg_arr["peg_left"]} {peg_arr["peg_mid"]} {peg_arr["peg_right"]}')
            result = solve_move(n - 1, helper, target, source)
            

            return moves
    result = solve_move(number_of_disks, peg_arr['peg_left'], peg_arr['peg_right'], peg_arr['peg_mid'])
    return '\n'.join(result)
       
hanoi_solver(2)
print(hanoi_solver(2))
        

        