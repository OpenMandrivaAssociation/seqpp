%define name seqpp
%define libname %mklibname %{name} 

Summary: A C++ library for performing biological sequence analysis
Name: %{name}
Version: 4.1.8
Release: %mkrel 5
Source0: http://stat.genopole.cnrs.fr/%{name}/download/%{name}-%{version}.tar.bz2
License: GPL
Group: Sciences/Biology
Url: http://stat.genopole.cnrs.fr/%{name}
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: gsl-devel doxygen tetex-latex gcc-c++ gcc-gfortran

%description
Seqpp is a C++ library providing a set of classes allowing 
Hidden Markov Model bases biological sequence analysis.


%package progs
Summary: Programs of the Seq++ Library
Group: Sciences/Biology
Requires: %{libname} = %{version}

%description progs
Contains the programs associated with the Seq++ library:
  - estim_m: performs Markov model estimation and/or statistics
computations on sequences.  
  - estim_pm: performs parcimonious markov estimations 
    on sequences.
  - simul_m: performs sequence generation using Markov models.



%package -n %{libname}
Summary: Shared libraries for the Seq++ Library
Group: System/Libraries
Provides: lib%{name} = %{version}-%{release}
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
Seqpp is a C++ library providing a set of classes allowing 
Hidden Markov Model based biological sequence analysis.


%package -n %{libname}-devel
Summary: Development libraries and headers for the Seq++ Library
Group: Development/C++
Requires: %{libname} = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{libname}-devel
Seqpp is a C++ library providing a set of classes allowing 
Hidden Markov Model based biological sequence analysis.


%prep

%setup -q

%build

%configure --enable-xml

%make
# %make docs

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# remove unwanted files
rm -f $RPM_BUILD_ROOT/%{_bindir}/dist_m
rm -f $RPM_BUILD_ROOT/%{_bindir}/estim_vlm
rm -f $RPM_BUILD_ROOT/%{_libdir}/libseqpp.so


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun  -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files progs
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man*/*
%{_datadir}/%{name}/alphabet/dna.alpha
%{_datadir}/%{name}/alphabet/protein.alpha
%doc AUTHORS COPYING README NEWS

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc AUTHORS COPYING README NEWS

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/seqpp/*.h
%{_libdir}/libseqpp.a
%{_libdir}/libseqpp.la
%doc AUTHORS COPYING README NEWS
# doc/latex/refman.ps doc/latex/refman.pdf doc/html




