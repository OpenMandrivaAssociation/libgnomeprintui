%define api 2-2
%define major 0
%define libname %mklibname gnomeprintui %{api} %{major}
%define develname %mklibname -d gnomeprintui %{api}

%define req_libgnomeprint_version 2.12.1

Summary:	GNOME print library
Name:		libgnomeprintui
Version:	2.18.6
Release:	5
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.levien.com/gnome/print-arch.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.18.3-2mdv use system-config-printer, not gnome-cups-add
Patch0:		libgnomeprintui-2.18.3-system-config-printer.patch

BuildRequires:	gnome-icon-theme >= 1.1.92
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	pkgconfig(libgnomeprint-2.2)
BuildRequires:	pkgconfig(libgnomecanvas-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)

Requires:	libgnomeprint >= 2.12.1
Requires:	gnome-icon-theme >= 1.1.92
Suggests:	system-config-printer

%description
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{libname}
Summary:	Library for GNOME print support
Group:		%{group}
Requires:	%{name} >= %{version}

%description -n %{libname}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{develname}
Summary:	Development libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname -d gnomeprintui 2-2 0} < 2.18.6-4

%description -n %{develname}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-gtk-doc
%make LIBS=-lm

%install
%makeinstall_std

%find_lang %{name}-2.2

%files -f %{name}-2.2.lang
%doc README AUTHORS NEWS
%{_datadir}/libgnomeprintui

%files -n %{libname}
%{_libdir}/libgnomeprintui-%{api}.so.%{major}*

%files -n %{develname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*



%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.18.6-4
+ Revision: 744913
- find_lang fix
- rebuild
- cleaned up spec
- employed api and major macros
- converted BRs to pkgconfig provides to avoid problems

* Mon Sep 19 2011 Götz Waschk <waschk@mandriva.org> 2.18.6-3
+ Revision: 700354
- rebuild

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.18.6-2
+ Revision: 660257
- mass rebuild

* Tue Sep 28 2010 Götz Waschk <waschk@mandriva.org> 2.18.6-1mdv2011.0
+ Revision: 581736
- update to new version 2.18.6

* Tue Mar 30 2010 Götz Waschk <waschk@mandriva.org> 2.18.5-1mdv2010.1
+ Revision: 529688
- update to new version 2.18.5

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.18.4-3mdv2010.1
+ Revision: 520859
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.18.4-2mdv2010.0
+ Revision: 425557
- rebuild

* Fri Mar 06 2009 Götz Waschk <waschk@mandriva.org> 2.18.4-1mdv2009.1
+ Revision: 349816
- update to new version 2.18.4

* Tue Sep 23 2008 Frederic Crozat <fcrozat@mandriva.com> 2.18.3-2mdv2009.0
+ Revision: 287192
- Patch0: use system-config-printer, not gnome-cups-add
- Remove hard dependency on gnome-cups-manager, switch to suggests on system-config-printer

* Mon Sep 22 2008 Götz Waschk <waschk@mandriva.org> 2.18.3-1mdv2009.0
+ Revision: 286817
- fix build
- new version
- drop patch, printerdrake is gone
- depend on gnome-cups-manager
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu Jan 31 2008 Götz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.1
+ Revision: 160645
- fix deps

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Oct 02 2007 Frederic Crozat <fcrozat@mandriva.com> 2.18.1-2mdv2008.0
+ Revision: 94712
- Patch0: call printerdrake instead of gnome-cups-add for Add button

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 89160
- new version
- new devel name


* Mon Mar 12 2007 Götz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 141992
- new version
- readd changelog

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Mon Feb 26 2007 Götz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126101
- new version

* Mon Feb 12 2007 Götz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 119932
- new version

* Mon Jan 22 2007 Götz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 112102
- new version

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 2.17.0-1mdv2007.1
+ Revision: 87671
- fix buildrequires
- new version
- Import libgnomeprintui

* Sat Sep 09 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-5mdv2007.0
- Fix conflicts (Mdv bug #24983)

* Wed Jun 21 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-4mdv2007.0
- Add conflicts to ease upgrade

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-3mdk
- use mkrel

* Mon Oct 10 2005 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.12.1-2mdk
- add BuildRequires: gtk-doc

* Fri Oct 07 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1
- Remove patch0 (merged upstream)

* Fri Sep 02 2005 Götz Waschk <waschk@mandriva.org> 2.10.2-3mdk
- rebuild to remove glitz dep

* Thu Aug 18 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 2.10.2-2mdk
- libtool fixes

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.2-1mdk 
- Release 2.10.2 (based on G�tz Waschk package)
- remove patch0 (merged upstream)

* Tue Dec 07 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- requires new libgnomeprint
- New release 2.8.2

* Mon Nov 29 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.1-1mdk
- update patch 0
- New release 2.8.1

* Tue Nov 09 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.8.0-1mdk
- New release 2.8.0
- Patch0 (Fedora): Asynchronously update PPD list

* Thu Jun 24 2004 G�tz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Fri Apr 23 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- New release 2.6.1

* Wed Apr 07 2004 <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- New release 2.6.0 (with G�tz help)

