"""
# Smart AST

Provides compatibility between AST 2 and 3.
"""
import os
import sys
from typing import Any


if os.environ.get("PYTHON_VER", "3") == "3":
    if sys.version_info >= (3, 8):
        from ast import (  # pylint: disable=no-name-in-module
            Add,
            alias,
            And,
            arg,
            arguments,
            Assign,
            AST,
            AsyncFunctionDef,
            Attribute,
            Await,
            BinOp,
            BitAnd,
            BitOr,
            BitXor,
            BoolOp,
            Bytes,
            Call,
            ClassDef,
            Compare,
            comprehension,
            Constant,
            Dict,
            DictComp,
            Div,
            Ellipsis as ASTEllipsis,
            Eq,
            expr,
            FloorDiv,
            FormattedValue,
            FunctionDef,
            GeneratorExp,
            get_docstring,
            Gt,
            GtE,
            IfExp,
            Import,
            ImportFrom,
            In,
            Index,
            Invert,
            Is,
            IsNot,
            JoinedStr,
            keyword,
            Lambda,
            List,
            ListComp,
            LShift,
            Lt,
            LtE,
            Mod,
            Module,
            Mult,
            Name,
            NameConstant,
            NodeVisitor,
            Not,
            NotEq,
            NotIn,
            Num,
            Or,
            parse,
            Pow,
            RShift,
            Set,
            SetComp,
            Slice,
            Starred,
            stmt,
            Str,
            Sub,
            Subscript,
            Tuple,
            UAdd,
            UnaryOp,
            USub,
            Yield,
            YieldFrom,
        )
    else:
        from typed_ast.ast3 import (  # pylint: disable=no-name-in-module
            Add,
            alias,
            And,
            arg,
            arguments,
            Assign,
            AST,
            AsyncFunctionDef,
            Attribute,
            Await,
            BinOp,
            BitAnd,
            BitOr,
            BitXor,
            BoolOp,
            Bytes,
            Call,
            ClassDef,
            Compare,
            Constant,
            comprehension,
            Dict,
            DictComp,
            Div,
            Ellipsis as ASTEllipsis,
            Eq,
            expr,
            FloorDiv,
            FormattedValue,
            FunctionDef,
            GeneratorExp,
            get_docstring,
            Gt,
            GtE,
            IfExp,
            Import,
            ImportFrom,
            In,
            Index,
            Invert,
            Is,
            IsNot,
            JoinedStr,
            keyword,
            Lambda,
            List,
            ListComp,
            LShift,
            Lt,
            LtE,
            Mod,
            Module,
            Mult,
            Name,
            NameConstant,
            NodeVisitor,
            Not,
            NotEq,
            NotIn,
            Num,
            Or,
            parse,
            Pow,
            RShift,
            Set,
            SetComp,
            Slice,
            Starred,
            stmt,
            Str,
            Sub,
            Subscript,
            Tuple,
            UAdd,
            UnaryOp,
            USub,
            Yield,
            YieldFrom,
        )
else:
    from typed_ast.ast27 import (  # pylint: disable=no-name-in-module
        Add,
        alias,
        And,
        arguments,
        Assign,
        AST,
        AsyncFunctionDef,
        Attribute,
        Await,
        BinOp,
        BitAnd,
        BitOr,
        BitXor,
        BoolOp,
        Call,
        ClassDef,
        Compare,
        comprehension,
        Dict,
        DictComp,
        Div,
        Ellipsis as ASTEllipsis,
        Eq,
        expr,
        FloorDiv,
        FunctionDef,
        GeneratorExp,
        get_docstring,
        Gt,
        GtE,
        IfExp,
        Import,
        ImportFrom,
        In,
        Index,
        Invert,
        Is,
        IsNot,
        keyword,
        Lambda,
        List,
        ListComp,
        LShift,
        Lt,
        LtE,
        Mod,
        Module,
        Mult,
        Name,
        NodeVisitor,
        Not,
        NotEq,
        NotIn,
        Num,
        Or,
        parse,
        Pow,
        RShift,
        Set,
        SetComp,
        Slice,
        stmt,
        Str,
        Sub,
        Subscript,
        Tuple,
        UAdd,
        UnaryOp,
        USub,
        Yield,
        YieldFrom,
    )

    arg = Any
    Bytes = Any
    Constant = Str
    NameConstant = Any
    Starred = Any
    JoinedStr = Any
    FormattedValue = Any

__all__ = [
    "Add",
    "alias",
    "And",
    "arg",
    "arguments",
    "Assign",
    "AST",
    "AsyncFunctionDef",
    "Attribute",
    "Await",
    "BinOp",
    "BitAnd",
    "BitOr",
    "BitXor",
    "BoolOp",
    "Bytes",
    "Call",
    "ClassDef",
    "Compare",
    "comprehension",
    "Constant",
    "Dict",
    "DictComp",
    "Div",
    "ASTEllipsis",
    "Eq",
    "expr",
    "FloorDiv",
    "FormattedValue",
    "FunctionDef",
    "GeneratorExp",
    "get_docstring",
    "Gt",
    "GtE",
    "IfExp",
    "Import",
    "ImportFrom",
    "In",
    "Index",
    "Invert",
    "Is",
    "IsNot",
    "JoinedStr",
    "keyword",
    "Lambda",
    "List",
    "ListComp",
    "LShift",
    "Lt",
    "LtE",
    "Mod",
    "Module",
    "Mult",
    "Name",
    "NameConstant",
    "NodeVisitor",
    "Not",
    "NotEq",
    "NotIn",
    "Num",
    "Or",
    "parse",
    "Pow",
    "RShift",
    "Set",
    "SetComp",
    "Slice",
    "Starred",
    "stmt",
    "Str",
    "Sub",
    "Subscript",
    "Tuple",
    "UAdd",
    "UnaryOp",
    "USub",
    "Yield",
    "YieldFrom",
]
