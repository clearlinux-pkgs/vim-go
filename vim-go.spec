Name     : vim-go
Version  : 1.23
Release  : 16
URL      : https://github.com/fatih/vim-go/archive/v1.23/vim-go-1.23.tar.gz
Source0  : https://github.com/fatih/vim-go/archive/v1.23/vim-go-1.23.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause

%description
# vim-go
Go (golang) support for Vim, which comes with pre-defined sensible settings (like
auto gofmt on save), with autocomplete, snippet support, improved syntax
highlighting, go toolchain commands, and more.  If needed vim-go installs all
necessary binaries for providing seamless Vim integration with current
commands. It's highly customizable and each individual feature can be
disabled/enabled easily.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/vim/vim82
cp -ar {autoload,compiler,doc,ftdetect,ftplugin,indent,plugin,syntax,templates} \
    %{buildroot}/usr/share/vim/vim82

%files
%defattr(-,root,root,-)
/usr/share/vim/vim82/autoload/ctrlp/decls.vim
/usr/share/vim/vim82/autoload/fzf/decls.vim
/usr/share/vim/vim82/autoload/go/alternate.vim
/usr/share/vim/vim82/autoload/go/asmfmt.vim
/usr/share/vim/vim82/autoload/go/auto.vim
/usr/share/vim/vim82/autoload/go/cmd.vim
/usr/share/vim/vim82/autoload/go/cmd_test.vim
/usr/share/vim/vim82/autoload/go/complete.vim
/usr/share/vim/vim82/autoload/go/complete_test.vim
/usr/share/vim/vim82/autoload/go/config.vim
/usr/share/vim/vim82/autoload/go/config_test.vim
/usr/share/vim/vim82/autoload/go/coverage.vim
/usr/share/vim/vim82/autoload/go/debug.vim
/usr/share/vim/vim82/autoload/go/debug_test.vim
/usr/share/vim/vim82/autoload/go/decls.vim
/usr/share/vim/vim82/autoload/go/def.vim
/usr/share/vim/vim82/autoload/go/def_test.vim
/usr/share/vim/vim82/autoload/go/doc.vim
/usr/share/vim/vim82/autoload/go/fillstruct.vim
/usr/share/vim/vim82/autoload/go/fillstruct_test.vim
/usr/share/vim/vim82/autoload/go/fmt.vim
/usr/share/vim/vim82/autoload/go/fmt_test.vim
/usr/share/vim/vim82/autoload/go/guru.vim
/usr/share/vim/vim82/autoload/go/guru_test.vim
/usr/share/vim/vim82/autoload/go/highlight_test.vim
/usr/share/vim/vim82/autoload/go/iferr.vim
/usr/share/vim/vim82/autoload/go/impl.vim
/usr/share/vim/vim82/autoload/go/impl_test.vim
/usr/share/vim/vim82/autoload/go/implements.vim
/usr/share/vim/vim82/autoload/go/import.vim
/usr/share/vim/vim82/autoload/go/import_test.vim
/usr/share/vim/vim82/autoload/go/indent_test.vim
/usr/share/vim/vim82/autoload/go/issue.vim
/usr/share/vim/vim82/autoload/go/job.vim
/usr/share/vim/vim82/autoload/go/job_test.vim
/usr/share/vim/vim82/autoload/go/keyify.vim
/usr/share/vim/vim82/autoload/go/lint.vim
/usr/share/vim/vim82/autoload/go/lint_test.vim
/usr/share/vim/vim82/autoload/go/list.vim
/usr/share/vim/vim82/autoload/go/lsp.vim
/usr/share/vim/vim82/autoload/go/lsp/completionitemkind.vim
/usr/share/vim/vim82/autoload/go/lsp/lsp.vim
/usr/share/vim/vim82/autoload/go/lsp/lsp_test.vim
/usr/share/vim/vim82/autoload/go/lsp/message.vim
/usr/share/vim/vim82/autoload/go/lsp_test.vim
/usr/share/vim/vim82/autoload/go/mod.vim
/usr/share/vim/vim82/autoload/go/package.vim
/usr/share/vim/vim82/autoload/go/package_test.vim
/usr/share/vim/vim82/autoload/go/path.vim
/usr/share/vim/vim82/autoload/go/play.vim
/usr/share/vim/vim82/autoload/go/promise.vim
/usr/share/vim/vim82/autoload/go/promise_test.vim
/usr/share/vim/vim82/autoload/go/referrers.vim
/usr/share/vim/vim82/autoload/go/rename.vim
/usr/share/vim/vim82/autoload/go/statusline.vim
/usr/share/vim/vim82/autoload/go/tags.vim
/usr/share/vim/vim82/autoload/go/tags_test.vim
/usr/share/vim/vim82/autoload/go/template.vim
/usr/share/vim/vim82/autoload/go/template_test.vim
/usr/share/vim/vim82/autoload/go/term.vim
/usr/share/vim/vim82/autoload/go/term_test.vim
/usr/share/vim/vim82/autoload/go/test-fixtures/cmd/bad.go
/usr/share/vim/vim82/autoload/go/test-fixtures/complete/complete.go
/usr/share/vim/vim82/autoload/go/test-fixtures/config/buildtags/buildtags.go
/usr/share/vim/vim82/autoload/go/test-fixtures/config/buildtags/constrainedfoo.go
/usr/share/vim/vim82/autoload/go/test-fixtures/config/buildtags/foo.go
/usr/share/vim/vim82/autoload/go/test-fixtures/config/buildtags/go.mod
/usr/share/vim/vim82/autoload/go/test-fixtures/debug/compilerror/main.go
/usr/share/vim/vim82/autoload/go/test-fixtures/debug/debugmain/debugmain.go
/usr/share/vim/vim82/autoload/go/test-fixtures/def/jump.go
/usr/share/vim/vim82/autoload/go/test-fixtures/fmt/hello.go
/usr/share/vim/vim82/autoload/go/test-fixtures/fmt/hello_golden.go
/usr/share/vim/vim82/autoload/go/test-fixtures/fmt/src/imports
"/usr/share/vim/vim82/autoload/go/test-fixtures/job/dir has spaces/main.go"
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/errcheck/compilererror/compilererror.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/errcheck/errcheck.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/errcheck/errcheck_test.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/foo/foo.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/baz.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/golangci-lint/problems/importabs/ok.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/golangci-lint/problems/importabs/problems.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/golangci-lint/problems/multiple/problems.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/golangci-lint/problems/shadow/problems.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/lint.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/lint/quux.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/vet/compilererror/compilererror.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lint/src/vet/vet.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lsp/fmt/format.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lsp/fmt/format_golden.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lsp/imports/imports.go
/usr/share/vim/vim82/autoload/go/test-fixtures/lsp/imports/imports_golden.go
/usr/share/vim/vim82/autoload/go/test-fixtures/package/src/package/bar/.gitkeep
/usr/share/vim/vim82/autoload/go/test-fixtures/package/src/package/baz/.gitkeep
/usr/share/vim/vim82/autoload/go/test-fixtures/package/src/package/go.mod
/usr/share/vim/vim82/autoload/go/test-fixtures/package/src/package/package.go
/usr/share/vim/vim82/autoload/go/test-fixtures/package/src/package/vendor/foo/.gitkeep
/usr/share/vim/vim82/autoload/go/test-fixtures/tags/add_all_golden.go
/usr/share/vim/vim82/autoload/go/test-fixtures/tags/add_all_golden_options.go
/usr/share/vim/vim82/autoload/go/test-fixtures/tags/add_all_input.go
/usr/share/vim/vim82/autoload/go/test-fixtures/tags/remove_all_golden.go
/usr/share/vim/vim82/autoload/go/test-fixtures/tags/remove_all_input.go
/usr/share/vim/vim82/autoload/go/test-fixtures/term/term.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/.gitignore
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/compilerror/compilerror.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/example/example_test.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/play/mock/controller.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/play/play_test.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/showname/showname_test.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/testcompilerror/testcompilerror_test.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/timeout/timeout_test.go
/usr/share/vim/vim82/autoload/go/test-fixtures/test/src/veterror/veterror.go
/usr/share/vim/vim82/autoload/go/test.vim
/usr/share/vim/vim82/autoload/go/test_test.vim
/usr/share/vim/vim82/autoload/go/textobj.vim
/usr/share/vim/vim82/autoload/go/tool.vim
/usr/share/vim/vim82/autoload/go/tool_test.vim
/usr/share/vim/vim82/autoload/go/ui.vim
/usr/share/vim/vim82/autoload/go/uri.vim
/usr/share/vim/vim82/autoload/go/uri_test.vim
/usr/share/vim/vim82/autoload/go/util.vim
/usr/share/vim/vim82/autoload/gotest.vim
/usr/share/vim/vim82/autoload/unite/sources/decls.vim
/usr/share/vim/vim82/compiler/go.vim
/usr/share/vim/vim82/doc/vim-go.txt
/usr/share/vim/vim82/ftdetect/gofiletype.vim
/usr/share/vim/vim82/ftplugin/asm.vim
/usr/share/vim/vim82/ftplugin/go.vim
/usr/share/vim/vim82/ftplugin/go/commands.vim
/usr/share/vim/vim82/ftplugin/go/mappings.vim
/usr/share/vim/vim82/ftplugin/go/snippets.vim
/usr/share/vim/vim82/ftplugin/go/tagbar.vim
/usr/share/vim/vim82/ftplugin/gohtmltmpl.vim
/usr/share/vim/vim82/ftplugin/gomod.vim
/usr/share/vim/vim82/ftplugin/gomod/commands.vim
/usr/share/vim/vim82/ftplugin/gomod/mappings.vim
/usr/share/vim/vim82/indent/go.vim
/usr/share/vim/vim82/indent/gohtmltmpl.vim
/usr/share/vim/vim82/plugin/go.vim
/usr/share/vim/vim82/syntax/go.vim
/usr/share/vim/vim82/syntax/godebugoutput.vim
/usr/share/vim/vim82/syntax/godebugstacktrace.vim
/usr/share/vim/vim82/syntax/godebugvariables.vim
/usr/share/vim/vim82/syntax/godefstack.vim
/usr/share/vim/vim82/syntax/gohtmltmpl.vim
/usr/share/vim/vim82/syntax/gomod.vim
/usr/share/vim/vim82/syntax/gotexttmpl.vim
/usr/share/vim/vim82/syntax/vimgo.vim
/usr/share/vim/vim82/templates/hello_world.go
/usr/share/vim/vim82/templates/hello_world_test.go
