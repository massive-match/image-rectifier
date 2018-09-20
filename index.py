from internal import args, resize

args = args.get_args()

print(resize.resize(args.input, args.output))