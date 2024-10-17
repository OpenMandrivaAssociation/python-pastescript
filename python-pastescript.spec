%define tarname PasteScript

Summary:	A pluggable command-line frontend
Name:		python-pastescript
Version:	1.7.5
Release:	3
Source0:	http://pypi.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
License:	MIT 
Group:		Development/Python
Url:		https://pythonpaste.org/script/
BuildArch:	noarch
Requires:	python-paste >= 1.3
Requires:	python-pastedeploy
Requires:	python-pkg-resources
BuildRequires:	python-setuptools, python-sphinx
BuildRequires:	python-pastedeploy

%description
PasteScript is a pluggable command-line tool. Included features:

* Create file layouts for packages. For instance, 
  paster create --template=basic_package MyPackage 
  will create a setuptools-ready file layout.
* Serve up web applications with configurations based on 
  paste.deploy.

%prep
%setup -q -n %{tarname}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sphinx-build -b html docs html
sed -i 's/.*egg-info$//' FILE_LIST
sed -i 's@tests/__init__py$@@' FILE_LIST
rm -f %{py_puresitedir}/tests/__init__.py

%files -f FILE_LIST
%doc html/
