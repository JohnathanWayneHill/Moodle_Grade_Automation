def time_to_sleep():  # catch me if you can
    round = random.randint(1, 4)
    num = random.uniform(0, 10)
    const = 10 ** round
    num_round = (((num) * const) // 1) / const
    print(num_round)
    time.sleep(num_round)
