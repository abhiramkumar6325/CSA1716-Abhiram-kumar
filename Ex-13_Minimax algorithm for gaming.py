import random
def minimax(secret_number, depth, is_maximizing):
    if depth == 0:
        return 0
    if is_maximizing:
        best_score = float('-inf')
        for guess in range(1, 11):
            score = minimax(secret_number, depth - 1, False)
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for guess in range(1, 11):
            score = minimax(secret_number, depth - 1, True)
            best_score = min(score, best_score)
        return best_score
def main():
    print("Welcome to the Number Guessing Game!")
    secret_number = random.randint(1, 10)
    max_depth = 8
    
    while True:
        guess = int(input("Enter your guess (1-10): "))
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("Congratulations! You guessed the secret number!")
            break

if __name__ == "__main__":
    main()
