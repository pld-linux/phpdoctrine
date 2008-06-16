%define		_pearname	Doctrine
Summary:	Package that uses webapps configuration
Name:		phpdoctrine
Version:	0.10.4
Release:	0.1
License:	LGPL
Group:		Applications/WWW
Source0:	http://www.phpdoctrine.org/downloads/Doctrine-%{version}.tgz
# Source0-md5:	0da208446b5027e4f8c105fddb468aea
URL:		http://www.phpdoctrine.org/
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common >= 5:4.2.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# _phpdocdir / php_docdir / phpdoc_dir ?
%define		_phpdocdir		%{_docdir}/phpdoc

%description
Doctrine is a PHP ORM (object relational mapper) for PHP 5.2.3+ that
sits on top of a powerful PHP DBAL (database abstraction layer). One
of its key features is the ability to optionally write database
queries in an OO (object oriented) SQL-dialect called DQL inspired by
Hibernates HQL. This provides developers with a powerful alternative
to SQL that maintains a maximum of flexibility without requiring
needless code duplication.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%package manual
Summary:	Tutorial for %{name}
Group:		Documentation

%description manual
Manual for %{name}.

%prep
%setup -qc
mv %{_pearname}-%{version}/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{php_pear_dir}/tests/%{_pearname},%{_phpdocdir}/%{name}}
cp -a lib/* $RPM_BUILD_ROOT%{php_data_dir}
cp -a tests/* $RPM_BUILD_ROOT%{php_pear_dir}/tests/%{_pearname}
cp -a manual/* $RPM_BUILD_ROOT%{_phpdocdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG COPYRIGHT LICENSE
%{php_data_dir}/Doctrine.php
%{php_data_dir}/Doctrine

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*

%files manual
%defattr(644,root,root,755)
%{_phpdocdir}/*
