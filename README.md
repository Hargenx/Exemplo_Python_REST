# Exemplo_Python_REST

REST (Representational State Transfer) é um estilo de arquitetura de software para sistemas distribuídos, como aplicações web. Ele se baseia em princípios de comunicação de hipermídia, ou seja, recursos de uma aplicação são identificados por URLs e são acessados ​​através de métodos HTTP (como GET, POST, PUT e DELETE). O objetivo do REST é tornar a comunicação entre sistemas mais fácil e escalável.

Neste exemplo, o aplicativo Flask implementa quatro rotas, cada uma corresponde a um método HTTP:  GET, POST, PUT, DELETE
<ul>
<li>GET /items: retorna uma lista de itens.</li>
<li>POST /items: cria um novo item.</li>
<li>PUT /items/<name>: atualiza o item com o nome especificado.</li>
<li>DELETE /items/<name>: exclui o item com o nome especificado.</li>
</ul>
