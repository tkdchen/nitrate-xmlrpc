%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%global pkg_name nitrate-xmlrpc
%global pkg_name_pyconverted nitrate_xmlrpc
%global pkg_module_name nitratexmlrpc

Name:           python-%{pkg_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        XMLRPC API for Nitrate

Group:          Development/Languages
License:        GPLv2+
URL:            https://github.com/tkdchen/nitrate-xmlrpc
Source0:        %{pkg_name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       python-nitrate


%description
XMLRPC Service for Nitrate, which allows scripts in client side to operate
Nitrate via XMLRPC calls.


%prep
%setup -q -n %{pkg_name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc CHANGES.txt LICENSE.txt MANIFEST.in README.rst TODO.txt VERSION.txt
%{python_sitelib}/%{pkg_module_name}/
%{python_sitelib}/%{pkg_name_pyconverted}-%{version}-py*.egg-info/


%changelog
