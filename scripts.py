import os

LIST_PATH = os.path.join(os.path.dirname(__file__), 'SpotifyBlocklist.txt')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), 'config.js')

if __name__ == "__main__":
    lines = []
    output_lines = []
    with open(LIST_PATH, 'r') as file:
        lines = file.readlines()

    for line in lines:
        # "DOMAIN-SUFFIX,baidu.com,DIRECT",
        line = line.strip()
        if (line != ''):
            output_lines.append(f'\t"DOMAIN, {line}, REJECT",')


    with open(OUTPUT_PATH, 'w') as file:
        file.write('const prependRule = [\n')
        file.write('\n'.join(output_lines))
        file.write('\n];')
    


    