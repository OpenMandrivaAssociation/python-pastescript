%define tarname PasteScript
%define name	python-pastescript
%define version	1.7.3
%define release 4

Summary:	A pluggable command-line frontend
Name:		%{name}
Version:	1.7.5
Release:	1
Source0:	http://pypi.python.org/packages/source/P/PasteScript/PasteScript-%{version}.tar.gz
License:	MIT 
Group:		Development/Python
Url:		http://pythonpaste.org/script/
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

%files -f FILE_LIST
%defattr(-,root,root)
%doc html/


%changelog
* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 1.7.3-3mdv2011.0
+ Revision: 649509
- Require pkg_resources.

* Thu Mar 31 2011 Lev Givon <lev@mandriva.org> 1.7.3-2
+ Revision: 649469
- Fix dependencies.

* Tue Nov 09 2010 Lev Givon <lev@mandriva.org> 1.7.3-1mdv2011.0
+ Revision: 595414
- import python-pastescript



