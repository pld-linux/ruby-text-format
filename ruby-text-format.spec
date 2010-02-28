%define pkgname text-format
Summary:	A Ruby port of Text::Format
Summary(pl.UTF-8):	Port Text::Format dla języka Ruby
Name:		ruby-%{pkgname}
Version:	1.0.0
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7b08f134e605da252c23afedbb481beb
URL:		http://www.halostatue.ca/ruby/Text__Format.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
%{?ruby_mod_ver_requires_eq}
Obsoletes:	ruby-Text-Format
Provides:	ruby-Text-Format
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
Summary:	Documentation files for %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
Documentation files for %{pkgname}.

%prep
%setup -q -c
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README  -o -print | xargs touch --reference %{SOURCE0}

%build
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib
# rm -rf ri/NOT_THIS_MODULE_RELATED_DIRS
rm -f ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}/%{name}-%{version}}

cp -a lib/* $RPM_BUILD_ROOT%{ruby_rubylibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}
%{ruby_ridir}/Text
