%define real_name FileHandle-Unget
%define	name perl-%{real_name}
%define	version 0.1622
%define	release %mkrel 1

Summary:    Perl modules that allow to place back more than one byte on a Filehandle
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
FileHandle::Unget is a perl module that is a drop-in replacement for the 
standard FileHandle perl module. It allows more than one byte to be placed back
on the input.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES LICENSE README
%{perl_vendorlib}/FileHandle/Unget.pm
%{_mandir}/man3/*

