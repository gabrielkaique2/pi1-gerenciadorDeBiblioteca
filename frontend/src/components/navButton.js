'use client'
import styles from './navButton.module.css'
import Link from "next/link"

import { usePathname } from 'next/navigation'

export default function Registrar( {link, titulo} ) {
    const pathname = usePathname();

    return(
        <Link className={pathname === link ? styles.activeLinkButton : styles.linkButton} href={link}>
            {titulo}
        </Link>
    )
}