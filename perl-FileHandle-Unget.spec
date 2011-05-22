%define upstream_name    FileHandle-Unget
%define	upstream_version 0.1623

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:    Perl modules that allow to place back more than one byte on a Filehandle
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
FileHandle::Unget is a perl module that is a drop-in replacement for the 
standard FileHandle perl module. It allows more than one byte to be placed back
on the input.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
