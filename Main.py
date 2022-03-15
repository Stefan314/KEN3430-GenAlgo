from GGA import GGA


def main():
    # Change these to whatever is best for your problem
    pop_sz = 2000
    max_gens = 100
    pr_co = 0.6
    pr_mt = 0.15
    # TODO: Fill these 3 in
    base_gen = None
    sel_type = None
    problem = None

    gga = GGA(pop_sz, max_gens, pr_co, pr_mt, base_gen, sel_type, problem)
    best_ind = gga.run()
    # Let the best individual do something. Like running your problem and printing out the solution to your problem
    pass


if __name__ == '__main__':
    main()
