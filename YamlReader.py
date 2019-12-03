import yaml         # sudo -E pip3 install pyyaml

class YamlReader():
    def read(self, path):
        f = open(path, "r+")
        allstr = f.read()
        f.close()

        # kubernetes manifest ファイル向け
        # ---で分割する
        delimiter = "---"
        docs = allstr.split(delimiter)

        dics = []
        for doc in docs:
            if doc == delimiter:
                continue
            dic = yaml.load(doc)
            if dic == None:
                continue
            #print("dic={}".format(dic))
            dics.append(dic)
        return dics
