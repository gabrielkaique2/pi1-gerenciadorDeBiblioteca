'use client'
import { useState } from 'react'
import { setCookie } from 'nookies'
import jwtSimple from 'jwt-simple'
import styles from './login.module.css'
import Image from 'next/image'
import Logo from '../../assets/Logotipo.png'
const API_URL = 'http://127.0.0.1:8000/login'

export default function LoginPage() {
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [stayConnected, setStayConnected] = useState(false) // novo estado para a checkbox

  const handleSubmit = async (e) => {
    e.preventDefault()

    
    const mockUser = { id: '1', username: 'ADMIN', password: 'Univespdrp03@' }

    if (username === mockUser.username && password === mockUser.password) {
      const token = jwtSimple.encode(mockUser, 'your-secret-key')

      setCookie(null, 'token', token, {
        maxAge: stayConnected ? 6 * 30 * 24 * 60 * 60 : 24 * 60 * 60, // se stayConnected for verdadeiro, o cookie durará 6 meses, caso contrário, durará 1 dia
        path: '/',
      })

      window.location.href = '/consulta'
    } else {
      alert('Usuário ou senha incorretos')
    }
  }

  return (
    <body className={styles.body}>
      <div className={styles.logo}>
        <Image className={styles.img} src={ Logo } alt="logo" />
      </div>
      <div className={styles.containerLogin}>
        <div className={styles.login}>
          <h1 className={styles.h1}>Login</h1>
          <form onSubmit={handleSubmit} className={styles.inputs}>
            <input type="text" placeholder="Digite seu usuário" value={username} onChange={(e) => setUsername(e.target.value)} />
            <input className={styles.inputPassword} type="password" placeholder="Digite sua senha" value={password} onChange={(e) => setPassword(e.target.value)} />
            <label className={styles.label}>
              <div className={styles.checkboxWrapper14}>
                <input id="s1-14" type="checkbox" className={styles.switch} checked={stayConnected} onChange={(e) => setStayConnected(e.target.checked)} /> {/* atualizado para usar o estado stayConnected */}
                <label htmlFor="s1-14">Permanecer Conectado</label>
              </div>
            </label>
            <div className={styles.botao}>
              <button className={styles.button} type="submit">Entrar</button>
            </div>
          </form>
          <br />
        </div>
      </div>
    </body>
  )
}