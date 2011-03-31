%define tarname PasteScript
%define name	python-pastescript
%define version	1.7.3
%define release %mkrel 2

Summary:	A pluggable command-line frontend
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/P/%{tarname}/%{tarname}-%{version}.tar.gz
License:	MIT 
Group:		Development/Python
Url:		http://pythonpaste.org/script/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
Requires:	python-paste >= 1.3
Requires:	python-pastedeploy
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
sphinx-build -b html docs html

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc html/
