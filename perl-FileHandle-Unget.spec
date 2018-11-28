%define modname	FileHandle-Unget
%define	modver	0.1634

Summary:	Perl modules that allow to place back more than one byte on a Filehandle
Name:		perl-%{modname}
Epoch:		1
Version:	%perl_convert_version %{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(inc::Module::Install)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl-devel

%description
FileHandle::Unget is a perl module that is a drop-in replacement for the 
standard FileHandle perl module. It allows more than one byte to be placed back
on the input.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
%make_install

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/FileHandle/Unget.pm
%{_mandir}/man3/*

