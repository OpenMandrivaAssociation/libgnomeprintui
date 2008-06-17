%define lib_major   0
%define lib_name	%mklibname gnomeprintui 2-2 %{lib_major}
%define develname %mklibname -d gnomeprintui 2-2

%define req_libgnomeprint_version 2.12.1

Summary: GNOME print library
Name: libgnomeprintui
Version: 2.18.2
Release: %mkrel 2
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# (fc) 2.18.1-2mdv call printerdrake and not gnome-cups-add for Add printer button
Patch0: libgnomeprintui-2.18.1-printerdrake.patch
License: LGPL
Group: System/Libraries
Url: http://www.levien.com/gnome/print-arch.html
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libgnomeprint2-2-devel >= %{req_libgnomeprint_version}
BuildRequires: libgnomecanvas2-devel >= 1.117.0
BuildRequires: libglade2.0-devel
BuildRequires: gtk+2-devel >= 2.4.0
BuildRequires: gnome-icon-theme >= 1.1.92
BuildRequires: gtk-doc
BuildRequires: perl-XML-Parser
BuildRequires: autoconf2.5 >= 2.54
Requires: libgnomeprint >= %{req_libgnomeprint_version}
Requires: gnome-icon-theme >= 1.1.92
Conflicts: %{_lib}gnomeprintui2-2_0 < 2.12


%description
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{lib_name}
Summary:	Library for GNOME print support
Group:		%{group}
Requires: %{name} >= %{version}

%description -n %{lib_name}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %develname
Summary:	Static libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{name}2-2-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}-%{release}
Requires:	libgnomeprint2-2-devel >= %{req_libgnomeprint_version}
Requires:	libgnomecanvas2-devel >= 1.117.0
Obsoletes: %mklibname -d gnomeprintui 2-2 0

%description -n %develname
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html


%prep
%setup -q
%patch0 -p1 -b .printerdrake

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}-2.2

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
  
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%files -f %{name}-2.2.lang
%defattr(-,root,root)
%doc README AUTHORS NEWS 
%{_datadir}/libgnomeprintui

%files -n %{lib_name} 
%{_libdir}/libgnomeprintui-2-2.so.0*

%files -n %develname
%defattr(-,root,root)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*


