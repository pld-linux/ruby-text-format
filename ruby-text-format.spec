Summary:	A Ruby port of Text::Format
Summary(pl.UTF-8):	Port Text::Format dla języka Ruby
Name:		ruby-Text-Format
Version:	0.64
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://www.halostatue.ca/files/text-format-%{version}.tar.gz
# Source0-md5:	f9e1aa720f39fffd4c83aeae4ba9e90f
Source1:	setup.rb
URL:		http://www.halostatue.ca/ruby/Text__Format.html
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
BuildArch:	noarch
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Format provides strong text formatting capabilities to Ruby.
Based on Perl's Text::Format 0.52, it offers all of the functionality
of that module and new capabilities besides.

%description -l pl.UTF-8
Text::Format udostępnia potężne możliwości formatowania tekstu w
języku Ruby. Jest oparty na perlowym Text::Format 0.52 i oferuje całą
funkcjonalność tego modułu, a przy okazji nowe funkcje.

%prep
%setup -q -n text-format-%{version}
cp %{SOURCE1} .

%build
ruby setup.rb config \
	--siterubyver=%{ruby_rubylibdir}

ruby setup.rb setup
rdoc --inline-source --op rdoc lib
rdoc --ri --op ri lib

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir}}

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/*
%{ruby_ridir}/*
