from flask import flash, redirect, url_for, render_template
from . import bk
from .. import db
from ..forms import BookForm, UserBookForm
from ..models import Book
from flask_login import current_user

@bk.route('/book/add', methods=['GET', 'POST'])
def book_add():
    form = BookForm()

    if form.validate_on_submit():
        book = Book()
        book.name = form.name.data
        db.session.add(book)
        db.session.commit()
        flash('Livro cadastrado com sucesso', 'success')
        return redirect(url_for('.book_add'))

    return render_template('book/add.html', form=form)


@bk.route('/user/<int:id>/add-book', methods=['GET', 'POST'])
def user_add_book(id):
    form = UserBookForm()
    if form.validate_on_submit():
        #form.book.data form pois esta armazenado na instancia form
        #book pois o post envia o nome do livro pelo name "book"
        #data pois é a var que armazena o conteudo enviado pelo form
        book = Book.query.get(form.book.data)
        #acessa o usuario atual utilizando um registro da tabela users e
        # insere um dado na coluna books, definida no model User
        current_user.books.append(book)
        #este current user pode acessar qualquer elemento da tabela users
        db.session.add(current_user)
        db.session.commit()
        flash('Livro cadastrado com sucesso!', 'success')
        return redirect(url_for('.user_add_book', id=current_user.id))
        #current_user.*** usa a funcao current user
    return render_template('book/user_add_book.html', form=form)
