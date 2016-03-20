#
# Conditional build:
%bcond_without	doc			# don't build ri/rdoc

%define pkgname text-format
Summary:	A Ruby port of Text::Format
Summary(pl.UTF-8):	Port Text::Format dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.0.0
Release:	4
License:	GPL
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7b08f134e605da252c23afedbb481beb
URL:		https://rubygems.org/gems/text-format
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Provides:	ruby-Text-Format
Obsoletes:	ruby-Text-Format
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Format provides strong text formatting capabilities to Ruby.
Based on Perl's Text::Format 0.52, it offers all of the functionality
of that module and new capabilities besides.

%description -l pl.UTF-8
Text::Format udostępnia potężne możliwości formatowania tekstu w
języku Ruby. Jest oparty na perlowym Text::Format 0.52 i oferuje całą
funkcjonalność tego modułu, a przy okazji nowe funkcje.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}
# tgz

%build
%if %{with doc}
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib
rm ri/created.rid
rm ri/cache.ri
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}

%if %{with doc}
install -d $RPM_BUILD_ROOT{%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_vendorlibdir}/text
%{ruby_vendorlibdir}/text/format.rb
%{ruby_vendorlibdir}/text/format

%if %{with doc}
%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/Text
%endif
