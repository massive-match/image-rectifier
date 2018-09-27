from internal import args, resize

args = args.get_args()

if args.size == '700':
    print(resize.proccess700(args.input, args.output))
elif args.size == '1500':
    print(resize.proccess1500(args.input, args.output))
else:
    print(resize.proccess(args.input, args.output))