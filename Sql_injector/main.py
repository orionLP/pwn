import argparse as arg
import list_generators
import json

class StoreDictPair(arg.Action):
    def __call__(self, parser, namespace, values, option_string = None):
        setattr(namespace,self.dest,json.loads(values))

def create_input_parser() -> arg.ArgumentParser:
    parser = arg.ArgumentParser(description="This program will try to inject sql statements into web apps")
    parser.add_argument("url", help = "specify the url to send without query strings", type = str, default = None)
    parser.add_argument("list_type", help = "type of list to create the results", type = str, choices = ["logic"])
    parser.add_argument("request_type", help = "type of requeset to use ", default = "GET", type = str, choices = ["GET", "POST"])
    parser.add_argument("http_headers", help = "specify the value of some headers in the form of '{" + '"param1"' + ':"val1"}' + "'", action = StoreDictPair, default = None)
    parser.add_argument("parameters", help = "specify the value of the input parameters for the injector in the form of '{" + '"param1"' + ':"val1"}' + "'", action = StoreDictPair, default = None)
    parser.add_argument("-t", help = "transform the input using url encoding to avoid detection", action="store_true")
    return parser

def main() -> None:
    
    parser = create_input_parser()
    args = parser.parse_args()
    
    print(args)

main()