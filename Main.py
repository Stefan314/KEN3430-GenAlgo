from GGA import GGA


def main():
    # TODO: Fill these 3 in
    base_gen = None
    sel_type = None
    problem = None
    # TODO: Change first 4
    gga = GGA(pop_size=2000,
              max_generations=100,
              prob_co=0.6,
              prob_mut=0.15,
              base_gen=base_gen,
              sel_type=sel_type,
              problem=problem)
    best_ind = gga.run()
    # TODO: do sth with best_ind, idk
    pass


if __name__ == '__main__':
    main()
