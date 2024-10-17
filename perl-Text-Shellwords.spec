%define upstream_name    Text-Shellwords
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Thin wrapper around shellwords.pl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This used to be a wrapper around shellwords.pl, but has now been superseded by
Text::ParseWords. Use that module instead. If you use this module, it will
simply report the shellwords() function from Text::ParseWords.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Text
%{_mandir}/*/*

%changelog
* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 405715
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.08-6mdv2009.0
+ Revision: 242050
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-4mdv2008.0
+ Revision: 87030
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-3mdv2007.0
- Rebuild

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.08-2mdk
- Fix SPEC according to Perl Policy
    - Source URL

* Fri Nov 18 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-1mdk
- New release 1.08
- %%mkrel

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-3mdk 
- better url
- spec cleanup
- don't ship useless empty directories
- make test in %%check

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.07-2mdk
- fix buildrequires in a backward compatible way

* Thu Jun 03 2004 Per Ã˜yvind Karlsen <peroyvind@linux-mandrake.com> 1.07-1mdk
- 1.07

* Wed Apr 21 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.08-1mdk
- new version
- rpmbuildupdate aware

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-2mdk
- %%makeinstall_std macro
- no more exception

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 1.02-2mdk
- fixed dir ownership (distlint)

