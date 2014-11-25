#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Class
%define		pnam	XPath
%include	/usr/lib/rpm/macros.perl
Summary:	Class::XPath - module that adds XPath matching to object trees
Summary(pl.UTF-8):	Class::XPath - moduł dodający dopasowywanie XPath do drzew obiektów
Name:		perl-Class-XPath
Version:	1.4
Release:	2
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	22ff3d2536027f3a9f59c6eb849fa610
URL:		http://search.cpan.org/dist/Class-XPath/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds XPath-style matching to your object trees. This means
that you can find nodes using an XPath-esque query with "match()" from
anywhere in the tree. Also, the "xpath()" method returns a unique path
to a given node which can be used as an identifier.

%description -l pl.UTF-8
Ten moduł dodaje dopasowywanie w stylu XPath do drzew obiektów.
Oznacza to, że można szukać węzłów przy użyciu zapytania typu XPath
funkcją "match()" z każdego miejsca w drzewie. Ponadto metoda
"xpath()" zwraca unikalną ścieżkę do danego węzła, którą można używać
jako identyfikator.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/XPath.pm
%{_mandir}/man3/*
