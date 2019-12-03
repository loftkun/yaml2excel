# yaml2excel

make individual elements of yaml files (such as kubernetes manifests) into text boxes of Excel file

## prerequisites

```sh
$ pip3 install pyyaml
$ pip3 install xlsxwriter
```
## usage

```sh
# generate Excel file from yaml files
$ python3 yaml2excel.py ${path}

# check Excel file
$ ls yaml.xlsx
```

## example

```sh
# get target yaml files
$ git clone https://github.com/istio/istio.git

# get yaml2excel
$ git https://github.com/loftkun/yaml2excel.git
$ cd yaml2excel
$ pip3 install pyyaml
$ pip3 install xlsxwriter

# generate Excel file from yaml files
$ python3 yaml2excel.py ../istio/samples/bookinfo/platform/kube/
makeBook : yaml.xlsx
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-certificate.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-db.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-details-v2.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-details.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-ingress.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-mysql.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-ratings-discovery.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-ratings-v2-mysql-vm.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-ratings-v2-mysql.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-ratings-v2.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-ratings.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo-reviews-v2.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/bookinfo.yaml
appendSheet : ../test/istio/samples/bookinfo/platform/kube/productpage-nodeport.yaml
$

# check Excel file
$ ls yaml.xlsx
yaml.xlsx
$
```

![](sample.png)