Name:		texlive-texlive-it
Version:	58653
Release:	1
Summary:	TeX Live manual (Italian)
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-it.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-it.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive texlive-it package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/texlive/texlive-it/Makefile
%doc %{_texmfdistdir}/doc/texlive/texlive-it/texlive-it.html
%doc %{_texmfdistdir}/doc/texlive/texlive-it/texlive-it.pdf
%doc %{_texmfdistdir}/doc/texlive/texlive-it/texlive-it.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
