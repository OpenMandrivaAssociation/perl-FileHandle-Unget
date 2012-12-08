%define upstream_name    FileHandle-Unget
%define	upstream_version 0.1623

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Epoch:		1

Summary:	Perl modules that allow to place back more than one byte on a Filehandle
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	http://search.cpan.org/CPAN/authors/id/D/DC/DCOPPIT/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
FileHandle::Unget is a perl module that is a drop-in replacement for the 
standard FileHandle perl module. It allows more than one byte to be placed back
on the input.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc CHANGES LICENSE README
%{perl_vendorlib}/FileHandle/Unget.pm
%{_mandir}/man3/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.162.300-4mdv2012.0
+ Revision: 765243
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1:0.162.300-3
+ Revision: 764832
- bump release
- rebuilt for perl-5.14.x

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.1623

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.162.300-2
+ Revision: 676881
- rebuild

* Wed Sep 02 2009 Jérôme Quelin <jquelin@mandriva.org> 1:0.162.300-1mdv2011.0
+ Revision: 424341
- update to 0.1623
- bumping epoch
- rebuild using %%perl_convert_version

  + Michael Scherer <misc@mandriva.org>
    - better description, stolen from Debian

* Fri Jul 18 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.1622-1mdv2009.0
+ Revision: 238035
- update to new version 0.1622

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 0.1621-2mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1621-2mdv2008.0
+ Revision: 86405
- rebuild


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 0.1621-1mdv2007.0
- rebuild

* Mon Jul 11 2005 Oden Eriksson <oeriksson@mandriva.com> 0.1621-1mdk
- initial Mandriva package

