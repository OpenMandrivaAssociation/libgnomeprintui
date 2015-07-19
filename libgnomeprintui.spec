%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2-2
%define major	0
%define libname %mklibname gnomeprintui %{api} %{major}
%define devname %mklibname -d gnomeprintui %{api}

%define req_libgnomeprint_version 2.12.1

Summary:	GNOME print library
Name:		libgnomeprintui
Version:	2.18.6
Release:	13
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.levien.com/gnome/print-arch.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnomeprintui/%{url_ver}/%{name}-%{version}.tar.bz2
# (fc) 2.18.3-2mdv use system-config-printer, not gnome-cups-add
Patch0:		libgnomeprintui-2.18.3-system-config-printer.patch

BuildRequires:	gnome-icon-theme
BuildRequires:	gnome-icon-theme-devel
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

%package -n %{devname}
Summary:	Development libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{mklibname -d gnomeprintui 2-2 0} < 2.18.6-4

%description -n %{devname}
This package contains the development files for %{name}.

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

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

